from google.guide_reports import markdown_report
from slack.post import send_message_to
from slack.post import MARIJN_IM_ID
from slack.post import IMPACT_SPHERES_ID


def main():
    print('Retrieving report ... ')
    rep = markdown_report()
    print(rep)
    print('Sending report to agilityscales.slack.com ... ')
    send_message_to(MARIJN_IM_ID, rep)
    print('Done.')


if __name__ == '__main__':
    main()
