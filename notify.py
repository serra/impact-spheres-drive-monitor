from google.guide_reports import markdown_report
from slack.post import send_message_to
from slack.post import MARIJN_IM_ID
from slack.post import IMPACT_SPHERES_ID


def main():
    print('Retrieving report ... ')
    url = 'https://github.com/serra/impact-spheres-drive-monitor'
    footer = 'This message is posted automatically. ' + \
             'See {0} for details.'.format(url)
    msg = '{0}\n\n{1}'.format(markdown_report(), footer)
    print(msg)
    print('Sending report to agilityscales.slack.com ... ')
    send_message_to(MARIJN_IM_ID, msg)
    print('Done.')


if __name__ == '__main__':
    main()
