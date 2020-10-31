def registration_success_response_data(account):
    data = {}
    data['response'] = "User was registered successfully."
    data['email']    = account.email
    data['username'] = account.username

    return data
