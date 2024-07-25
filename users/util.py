import resend

def send_password_reset_email(user, token):
    resend.api_key = "re_RFCZPU5C_GHBS9tCy2jD9C4iCHu7F6Bf3"

    reset_link = f"http://tail_watch/password-reset-confirm/?uid={user.id}&token={token}"

    print(reset_link)
    
    resend.Emails.send({
        'subject':"Password Reset Request",
        'message':f"Click the link to reset your password: {reset_link}",
        'from':"onboarding@resend.dev",
        'to':f"{user.email}",
        'html':f"<p>Follow this link to reset your password {reset_link}<p>",
    })
