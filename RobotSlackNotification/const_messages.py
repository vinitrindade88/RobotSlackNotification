principal_block = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Aplicación en prueba:  OneApp Mobile",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": " || *Branch*: main || *Entorno*: qa"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Estado de la prueba:",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":red_circle: FAIL"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Resumen:",
            "emoji": True
        }
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Pruebas Ejecutadas:*\n17"
            },
            {
                "type": "mrkdwn",
                "text": "*Probado con éxito:*\n15"
            }
        ]
    },
    {
        "type": "section",
        "fields": [
            {
                "type": "mrkdwn",
                "text": "*Probado con error:*\n2"
            },
            {
                "type": "mrkdwn",
                "text": "*Pruebas salteadas:*\n0"
            }
        ]
    },
    {
        "type": "divider"
    },
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Siga la ejecución:",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*CICD*: *<https://google.com|0Ghry48>* || *BrowserStack*: *<https://google.com|0Ghry48>*"
        }
    }
]

start_suite_message = [
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Aplicación en prueba:  OneApp Mobile",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*Branch*: main || *Entorno*: qa"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Estado de la prueba",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": ":slack_load: *En Prueba*"
        }
    },
    {
        "type": "divider"
    },
    {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "Siga la ejecución:",
            "emoji": True
        }
    },
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "*CICD*: *<https://google.com|0Ghry48>* || *BrowserStack*: *<https://google.com|0Ghry48>*"
        }
    }
]

tread_error_message = [
    {
        "color": "ff4646",
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Cenário:  XPTO"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Mensaje*"
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "_Erro XPTO_"
                }
            }
        ]
    }
]

