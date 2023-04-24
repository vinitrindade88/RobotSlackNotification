import slack
from const_messages import principal_block, start_suite_message, tread_error_message
from env import SLACK_TOKEN, CHANNEL

ROBOT_LISTENER_API_VERSION = 3
ROBOT_LIBRARY_SCOPE = 'GLOBAL'
ROBOT_LIBRARY_VERSION = '1.2.0'

application = "OneApp Mobile"  #deve virar argumento do Listener
environment = "QA"  #deve virar argumento do Listener
branch = "main"  #deve virar argumento do Listener
test_url = "https://www.google.com/"  #deve virar argumento do Listener
cicd_id = "0Ghry48"  #deve virar argumento do Listener

## Initial State
executions = 0
success_executions = 0
failed_executions = 0
skipped_executions = 0
message_timestamp = []

client = slack.WebClient(token=SLACK_TOKEN)
channel_id = CHANNEL    #deve virar argumento do Listener


def start_suite(data, result):
    message = _build_principal_message(result, application, environment, executions, success_executions, failed_executions, skipped_executions)
    ts = _post_principal_message(result, message)
    message_timestamp.append(ts)


def end_suite(data, result):
    statistics = _robot_statistic(result.statistics)

    count_pass = statistics.passed
    count_failed = statistics.failed
    count_skipped = statistics.skipped
    count_total = statistics.total

    message = _build_principal_message(result, application, environment, count_total, count_pass, count_failed, count_skipped)
    _update_principal_message(result, message_timestamp[0], message)


def end_test(data, result):
    attachment_color = _attachment_color(result)
    message = _build_thread_message(result, attachment_color)
    _post_thread_message(result, message, message_timestamp[0])


def _robot_statistic(statistics):
    try:
        if statistics.total:
            return statistics                   # robotframework < 4.0.0
    except:
        return statistics.all                   # robotframework > 4.0.0


def _post_principal_message(result, message):
    if not result.parent:
        response = client.chat_postMessage(channel=channel_id, blocks=message)
        return response['ts']


def _post_thread_message(result, message, message_ts):
    if result.failed or result.skipped:
        client.chat_postMessage(channel=channel_id, attachments=message, thread_ts=message_ts)


def _update_principal_message(result, message_timestamp, message):
    if not result.parent:
        client.chat_update(channel=channel_id, blocks=message, ts=message_timestamp)


def _build_principal_message(result, application, environment, executions, success_executions, failed_executions, skipped_executions):
    '''
    Builds the main message block
    '''

    if result.passed == False and result.failed == False:
        start_suite_message[7]['text']['text'] = f'*CICD*: *<{test_url}|{cicd_id}>* || *BrowserStack*: *<{test_url}|{cicd_id}>*'

        return start_suite_message
    else:
        result_status = result.status

        if result.passed:
            result_icon = ":large_green_circle:"
        elif result.failed:
            result_icon = ":red_circle:"
        else:
            result_icon = ":white_circle:"

        principal_block[0]['text']['text'] = f'Aplicación en prueba:  {application}'
        principal_block[1]['text']['text'] = f'*Branch*: {branch} || *Enterno*: {environment}'
        principal_block[4]['text']['text'] = f'{result_icon} *{result_status}*'

        principal_block[7]['fields'][0]['text'] = f'*Pruebas Ejecutadas:*\n{executions}'
        principal_block[7]['fields'][1]['text'] = f'*Probado con éxito:*\n{success_executions}'

        principal_block[8]['fields'][0]['text'] = f'*Probado con error:*\n{failed_executions}'
        principal_block[8]['fields'][1]['text'] = f'*Pruebas salteadas:*\n{skipped_executions}'

        principal_block[11]['text']['text'] = f'*CICD*: *<{test_url}|{cicd_id}>* || *BrowserStack*: *<{test_url}|{cicd_id}>*'

        return principal_block


def _build_thread_message(result, attachment_color):

    tread_error_message[0]['color'] = f'{attachment_color}'
    tread_error_message[0]['blocks'][0]['text']['text'] = f'{result.name}'
    tread_error_message[0]['blocks'][3]['text']['text'] = f'{result.name}'

    return tread_error_message


def _attachment_color(result):
    color = None

    if result.passed:
        color = "1abf00"
    elif result.failed:
        color = "ff4646"
    elif result.skipped:
        color = "eddd00"

    return color



# class RobotframeworkSlackNotification:
#
#     def __init__(self):
#         self.client = slack.WebClient(token=SLACK_TOKEN)
#         self.channel_id = CHANNEL
#
#     def end_test(self, data, result):
#         if not result.passed:
#             print('Test "%s" failed: %s' % (result.name, result.message))
#             input('Press enter to continue.')

    # @keyword('Post Slack Message')
    # def post_slack_message(self, application, environment):
    #     message_timestamp = self._post_principal_message(application, environment)
    #     return message_timestamp
    #
    # @keyword('Update Slack Message')
    # def update_slack_message(self, message_timestamp, application, environment, executions, success_executions,
    #                          failed_executions):
    #     self._update_principal_message(message_timestamp, application, environment, executions, success_executions,
    #                                    failed_executions)
    #
    # def _post_principal_message(self, application, environment):
    #     self._build_principal_message(application, environment, executions, success_executions, failed_executions)
    #     response = self.client.chat_postMessage(channel=self.channel_id, blocks=principal_block)
    #     return response['ts']
    #
    # def _update_principal_message(self, message_timestamp, application, environment, executions, success_executions,
    #                               failed_executions):
    #     self._build_principal_message(application, environment, executions, success_executions, failed_executions)
    #     self.client.chat_update(channel=self.channel_id, blocks=principal_block, ts=message_timestamp)
    #
    # def _build_principal_message(self, application, environment, executions, success_executions, failed_executions):
    #     '''
    #     Builds the main message block
    #     '''
    #     principal_block[0]['text']['text'] = f':white_circle: Aplicación en prueba: {application} | [{environment}]'
    #     principal_block[3]['fields'][0]['text'] = f'*Estado:*\nEn Prueba'
    #     principal_block[3]['fields'][1]['text'] = f'*Pruebas Ejecutadas:*\n{executions}'
    #
    #     principal_block[4]['fields'][0]['text'] = f'*Probado con éxito:*\n{success_executions}'
    #     principal_block[4]['fields'][1]['text'] = f'*Probado con error:*\n{failed_executions}'
    #
    # def _get_message(self, ts):
    #     response = self.client.chat_getPermalink(channel=self.channel_id, message_ts=ts)
    #     print(response)
    #     if response.status_code == 200:
    #         return True
    #     else:
    #         return False


# if __name__ == "__main__":
#     sn = SlackNotification()
#     ts = sn.post_slack_message(application=application, environment=environment)
#     sn.update_slack_message(ts, application, environment, 1, 1, 0)
#     sn.update_slack_message(ts, application, environment, 2, 1, 1)
