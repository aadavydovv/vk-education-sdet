from test_api.base import ApiBase
import pytest


class TestSegments(ApiBase):
    @pytest.mark.API
    def test_segment_create(self):
        new_segment_id = self.api_client.post_segment_create()
        self.api_client.get_segment_check('create', new_segment_id)

    @pytest.mark.API
    def test_segment_delete(self):
        new_segment_id = self.api_client.post_segment_create()
        self.api_client.delete_segment(new_segment_id)
        self.api_client.get_segment_check('delete', new_segment_id)


class TestCampaigns(ApiBase):
    @pytest.mark.API
    def test_campaign_create(self):
        new_campaign_id = self.api_client.post_campaign_create()
        self.api_client.get_campaign_create_check(new_campaign_id)
