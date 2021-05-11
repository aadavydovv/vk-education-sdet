from mysql.models import AmountRequestsOverall, AmountRequestsByType, TopByUrl, TopBySizeWithClientError, \
    TopByIpWithServerError


class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def add_entry_amount_requests_overall(self, amount):
        entry = AmountRequestsOverall(amount=amount)
        self.client.session.add(entry)

    def add_entry_amount_requests_by_type(self, type_request, amount):
        entry = AmountRequestsByType(type_request=type_request, amount=amount)
        self.client.session.add(entry)

    def add_entry_top_by_url(self, url, amount_requests):
        entry = TopByUrl(url=url, amount_requests=amount_requests)
        self.client.session.add(entry)

    def add_entry_top_by_size_with_client_error(self, url, status, size, ip):
        entry = TopBySizeWithClientError(url=url, status=status, size=size, ip=ip)
        self.client.session.add(entry)

    def add_entry_top_by_ip_with_server_error(self, ip, amount_requests):
        entry = TopByIpWithServerError(ip=ip, amount_requests=amount_requests)
        self.client.session.add(entry)
