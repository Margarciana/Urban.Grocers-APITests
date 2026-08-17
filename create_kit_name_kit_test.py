
import sender_stand_request
from data import get_kit_body, name_1_char, name_with_spaces, name_numbers, name_0_chars, \
    name_512_chars, kit_body_no_name, name_511_chars, name_special_chars, kit_body_number_name


def positive_assert(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    kit_data = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_data.status_code == 201
    assert kit_data.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    kit_data = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert kit_data.status_code == 400

def test_create_1_char_kit_successfully():
    kit_body = get_kit_body(name_1_char)
    positive_assert(kit_body)

def test_create_511_char_kit_successfully():
    kit_body = get_kit_body(name_511_chars)
    positive_assert(kit_body)

def test_create_special_chars_kit_successfully():
    kit_body = get_kit_body(name_special_chars)
    positive_assert(kit_body)

def test_create_spaced_chars_kit_successfully():
    kit_body = get_kit_body(name_with_spaces)
    positive_assert(kit_body)

def test_create_kit_name_with_numbers_successfully():
    kit_body = get_kit_body(name_numbers)
    positive_assert(kit_body)

def test_create_0_chars_kit_name_unsuccessfully():
    kit_body = get_kit_body(name_0_chars)
    negative_assert_code_400(kit_body)

def test_create_512_chars_kit_name_unsuccessfully():
    kit_body = get_kit_body(name_512_chars)
    negative_assert_code_400(kit_body)

def test_create_kit_without_name_unsuccessfully():
    negative_assert_code_400(kit_body_no_name)

def test_create_kit_name_with_numbers_unsuccessfully():
    kit_body = kit_body_number_name
    negative_assert_code_400(kit_body)
