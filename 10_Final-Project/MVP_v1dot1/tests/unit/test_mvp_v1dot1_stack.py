import aws_cdk as core
import aws_cdk.assertions as assertions
from mvp_v1dot1.mvp_v1dot1_stack import MvpV1Dot1Stack


def test_sqs_queue_created():
    app = core.App()
    stack = MvpV1Dot1Stack(app, "mvp-v1dot1")
    template = assertions.Template.from_stack(stack)

    template.has_resource_properties("AWS::SQS::Queue", {
        "VisibilityTimeout": 300
    })


def test_sns_topic_created():
    app = core.App()
    stack = MvpV1Dot1Stack(app, "mvp-v1dot1")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("AWS::SNS::Topic", 1)
