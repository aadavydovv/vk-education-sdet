from pathlib import Path
import collections


class Script:
    def __init__(self, path_log_from_repo_root):
        path_log = Path(__file__).parents[2] / path_log_from_repo_root

        with open(path_log) as file_log:
            self.lines_log = [line.split(' ') for line in file_log.readlines()]

    def get_amount_requests_overall(self):
        return len(self.lines_log)

    def get_amount_requests_by_type(self):
        amount_requests_by_type = collections.defaultdict(lambda: 0)
        for line in self.lines_log:
            amount_requests_by_type[line[5][1:33]] += 1
        return amount_requests_by_type

    def get_top_by_url(self):
        return collections.Counter([line[6] for line in self.lines_log]).most_common(10)

    def get_top_by_size_with_client_error(self):
        lines_log_formatted = [[line[6], line[8], int(line[9]), line[0]]
                               for line in self.lines_log if line[8].startswith('4')]
        return sorted(lines_log_formatted, key=lambda x: (x[2]), reverse=True)[:5]

    def get_top_by_ip_with_server_error(self):
        lines_log_formatted = [line[0] for line in self.lines_log if line[8].startswith('5')]
        return collections.Counter(lines_log_formatted).most_common(5)
