from mysql.models import (AmountRequestsOverall, AmountRequestsByType, TopByUrl, TopBySizeWithClientError,
                          TopByIpWithServerError)
from test_mysql.base import MySQLBase


class TestMySQL(MySQLBase):

    def test_amount_requests_overall(self):
        amount_requests_overall = self.script.get_amount_requests_overall()
        self.mysql_builder.add_entry_amount_requests_overall(amount_requests_overall)

        assert self.mysql_client.session.query(AmountRequestsOverall).count() == 1

    def test_amount_requests_by_type(self):
        amount_requests_by_type = self.script.get_amount_requests_by_type()

        for entry in amount_requests_by_type:
            self.mysql_builder.add_entry_amount_requests_by_type(entry, amount_requests_by_type[entry])

        assert self.mysql_client.session.query(AmountRequestsByType).count() == 5

    def test_top_by_url(self):
        top_by_url = self.script.get_top_by_url()

        for entry in top_by_url:
            self.mysql_builder.add_entry_top_by_url(entry[0], entry[1])

        assert self.mysql_client.session.query(TopByUrl).count() == 10

    def test_top_by_size_with_client_error(self):
        top_by_size_with_client_error = self.script.get_top_by_size_with_client_error()

        for entry in top_by_size_with_client_error:
            self.mysql_builder.add_entry_top_by_size_with_client_error(entry[0], entry[1], entry[2], entry[3])

        assert self.mysql_client.session.query(TopBySizeWithClientError).count() == 5

    def test_top_by_ip_with_server_error(self):
        top_by_ip_with_server_error = self.script.get_top_by_ip_with_server_error()

        for entry in top_by_ip_with_server_error:
            self.mysql_builder.add_entry_top_by_ip_with_server_error(entry[0], entry[1])

        assert self.mysql_client.session.query(TopByIpWithServerError).count() == 5
