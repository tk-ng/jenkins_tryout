from behave import when  # pylint: disable=no-name-in-module
import allure
from allure_commons.types import AttachmentType


@when("we buy tickets")
def step_buy_tickets(context):
    """Step to buy tickets"""
    if context.ticket_count <= 0:
        return
    body = "Ticket(s) without park admission:"
    body += f"\n{context.ticket_count}"
    allure.attach(body, name="ticket_vid", attachment_type=AttachmentType.TEXT)


@when("we buy tickets with park admission")
def step_buy_tickets_w_park_admission(context):
    """Step to buy tickets and then enter park"""
    if context.ticket_entered_count <= 0:
        return
    body = "Ticket(s) with park admission:"
    body += f"\n{context.ticket_entered_count}"
    allure.attach(body, name="ticket_vid_w_pa", attachment_type=AttachmentType.TEXT)
