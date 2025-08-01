from behave import when  # pylint: disable=no-name-in-module
import allure
from allure_commons.types import AttachmentType


@when("we buy passes")
def step_buy_tickets(context):
    """Step to buy Magic Access passes"""
    if context.pass_count <= 0:
        return
    body = "Pass(es) without park admission:"
    body += f"\n{context.pass_count}"
    allure.attach(body, name="pass_vid", attachment_type=AttachmentType.TEXT)


@when("we buy passes with park admission")
def step_buy_tickets(context):
    """Step to buy Magic Access passes"""
    if context.pass_entered_count <= 0:
        return
    body = "Pass(es) with park admission:"
    body += f"\n{context.pass_entered_count}"
    allure.attach(body, name="pass_vid_w_pa", attachment_type=AttachmentType.TEXT)
