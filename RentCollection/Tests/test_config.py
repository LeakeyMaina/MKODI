
from ..Config import settings

def test_authorization_key():
    assert settings.authorization_key=="amJDTnBmakZ5UHdqVWRmWHpCNThGQW9CN3VMUkdDQnM6S2FIRUhlaTM3WUtXS2RDbA=="

def test_base_url():
    assert settings.base_url=="https://sandbox.safaricom.co.ke"

def test_confirmation_url():
    assert settings.confirmation_url=="https://soluhisho.com/confirmation"

def test_short_code():
    assert settings.short_code=="123456"

def test_response_type():
    assert settings.response_type=="Completed"

def test_validation_url():
    assert settings.validation_url=="https://soluhisho.com/validation"
