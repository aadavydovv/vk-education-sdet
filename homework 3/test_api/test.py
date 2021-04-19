from test_api.base import ApiBase
import pytest


class TestSegments(ApiBase):
    @pytest.mark.API
    def test_segment_create(self):
        self.api_client.post_segment_create()
        self.api_client.get_segment_check('create')

    @pytest.mark.API
    def test_segment_delete(self):
        self.test_segment_create()
        self.api_client.post_segment_delete()
        self.api_client.get_segment_check('delete')


class TestCampaigns(ApiBase):
    @pytest.mark.API
    def test_campaign_create(self):
        self.api_client.post_campaign_create()
        self.api_client.get_campaign_create_check()
