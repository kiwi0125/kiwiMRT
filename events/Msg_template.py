from line_bot_api import *

def show_red():
    flex_message = FlexSendMessage(
            alt_text="紅起訖站",
            contents={
                    "type": "carousel",
                    "contents": [
                        {
                        "type": "bubble",
                        "size": "giga",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "(紅線)請選擇起訖站：",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#FF004D",
                                "align": "center"
                            }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "separator"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "R3小港",
                                        "margin": "none",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md",
                                        "color": "#D71313",
                                        "offsetEnd": "none",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                        "type": "message",
                                        "label": "往北",
                                        "text": "小港往北"
                                        },
                                        "style": "primary",
                                        "offsetEnd": "none",
                                        "offsetTop": "none",
                                        "margin": "none",
                                        "gravity": "center",
                                        "offsetBottom": "none",
                                        "offsetStart": "none",
                                        "color": "#1D5D9B"
                                    }
                                    ],
                                    "spacing": "none",
                                    "margin": "none",
                                    "offsetBottom": "none",
                                    "paddingBottom": "none",
                                    "borderWidth": "none",
                                    "justifyContent": "space-evenly"
                                },
                                {
                                    "type": "separator",
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "R4",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "高雄國際機場",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "sm",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        }
                                        ],
                                        "justifyContent": "center",
                                        "alignItems": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "高雄國際機場往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "高雄國際機場往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "R4A草衙",
                                        "margin": "none",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md",
                                        "color": "#D71313",
                                        "offsetEnd": "none",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "草衙往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "草衙往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    }
                                    ],
                                    "spacing": "none",
                                    "margin": "none"
                                },
                                {
                                    "type": "separator",
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "R5",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "前鎮高中",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        }
                                        ],
                                        "justifyContent": "center",
                                        "alignItems": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "前鎮高中往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "前鎮高中往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "R6凱旋",
                                        "margin": "none",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md",
                                        "color": "#D71313",
                                        "offsetEnd": "none",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "凱旋往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "凱旋往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    }
                                    ],
                                    "spacing": "none",
                                    "margin": "none"
                                },
                                {
                                    "type": "separator",
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "R7獅甲",
                                        "margin": "none",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md",
                                        "color": "#D71313",
                                        "offsetEnd": "none",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "獅甲往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "獅甲往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "R8",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "三多商圈",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        }
                                        ],
                                        "justifyContent": "center",
                                        "alignItems": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "三多商圈往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "三多商圈往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    }
                                    ],
                                    "spacing": "none",
                                    "margin": "none"
                                },
                                {
                                    "type": "separator",
                                    "margin": "md"
                                }
                                ]
                            }
                            ]
                        }
                        },
                        {
                        "type": "bubble",
                        "size": "giga",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "(紅線)請選擇起訖站：",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#FF004D",
                                "align": "center"
                            }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "separator"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "R9",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "中央公園",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "sm",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        }
                                        ],
                                        "justifyContent": "center",
                                        "alignItems": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "中央公園往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "中央公園往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "R10",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "美麗島",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "sm",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        }
                                        ],
                                        "justifyContent": "center",
                                        "alignItems": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "美麗島往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "美麗島往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    }
                                    ],
                                    "spacing": "none",
                                    "margin": "none",
                                    "offsetBottom": "none",
                                    "paddingBottom": "none",
                                    "borderWidth": "none",
                                    "justifyContent": "space-evenly"
                                },
                                {
                                    "type": "separator",
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "R11",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "高雄車站",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "sm",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        }
                                        ],
                                        "justifyContent": "center",
                                        "alignItems": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "高雄車站往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "高雄車站往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "R12後驛",
                                        "margin": "none",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md",
                                        "color": "#D71313",
                                        "offsetEnd": "none",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "後驛往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "後驛往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    }
                                    ],
                                    "spacing": "none",
                                    "margin": "none"
                                },
                                {
                                    "type": "separator",
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "R13",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "凹子底",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        }
                                        ],
                                        "justifyContent": "center",
                                        "alignItems": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "凹子底往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "凹子底往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "R14巨蛋",
                                        "margin": "none",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md",
                                        "color": "#D71313",
                                        "offsetEnd": "none",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "巨蛋往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "巨蛋往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    }
                                    ],
                                    "spacing": "none",
                                    "margin": "none"
                                },
                                {
                                    "type": "separator",
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "R15",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "生態園區",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        }
                                        ],
                                        "justifyContent": "center",
                                        "alignItems": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "生態園區往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "生態園區往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "R16左營",
                                        "margin": "none",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md",
                                        "color": "#D71313",
                                        "offsetEnd": "none",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "左營往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "左營往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    }
                                    ],
                                    "spacing": "none",
                                    "margin": "none"
                                },
                                {
                                    "type": "separator",
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "R17世運",
                                        "margin": "none",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md",
                                        "color": "#D71313",
                                        "offsetEnd": "none",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "世運往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "世運往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "R18",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "油廠國小",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        }
                                        ],
                                        "justifyContent": "center",
                                        "alignItems": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "油廠國小往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "油廠國小往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    }
                                    ],
                                    "spacing": "none",
                                    "margin": "none"
                                }
                                ]
                            }
                            ]
                        }
                        },
                        {
                        "type": "bubble",
                        "size": "giga",
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "text": "(紅線)請選擇起訖站：",
                                "weight": "bold",
                                "size": "xl",
                                "color": "#FF004D",
                                "align": "center"
                            }
                            ]
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "separator"
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "R19",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "楠梓加工區",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "sm",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        }
                                        ],
                                        "justifyContent": "center",
                                        "alignItems": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "楠梓加工區往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "楠梓加工區往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "R20後勁",
                                        "margin": "none",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md",
                                        "color": "#D71313",
                                        "offsetEnd": "none",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "後勁往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "後勁往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    }
                                    ],
                                    "spacing": "none",
                                    "margin": "none"
                                },
                                {
                                    "type": "separator",
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "R21",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "都會公園",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        }
                                        ],
                                        "justifyContent": "center",
                                        "alignItems": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "都會公園往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "都會公園往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "text",
                                        "text": "R21青埔",
                                        "margin": "none",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md",
                                        "color": "#D71313",
                                        "offsetEnd": "none",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "青埔往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "青埔往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    }
                                    ],
                                    "spacing": "none",
                                    "margin": "none"
                                },
                                {
                                    "type": "separator",
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "R22A",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "橋頭糖廠",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        }
                                        ],
                                        "justifyContent": "center",
                                        "alignItems": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "橋頭糖廠往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "橋頭糖廠往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "xxl"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "R23",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "text",
                                            "text": "橋頭火車站",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#D71313",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        }
                                        ],
                                        "justifyContent": "center",
                                        "alignItems": "center"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "vertical",
                                        "contents": [
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往北",
                                            "text": "橋頭火車站往北"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往南",
                                            "text": "橋頭火車站往南"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#75C2F6"
                                        }
                                        ]
                                    }
                                    ],
                                    "spacing": "none",
                                    "margin": "none"
                                },
                                {
                                    "type": "separator",
                                    "margin": "md"
                                },
                                {
                                    "type": "box",
                                    "layout": "horizontal",
                                    "contents": [
                                    {
                                        "type": "text",
                                        "text": "R24南崗山",
                                        "margin": "none",
                                        "align": "center",
                                        "gravity": "center",
                                        "size": "md",
                                        "color": "#D71313",
                                        "offsetEnd": "none",
                                        "weight": "bold"
                                    },
                                    {
                                        "type": "button",
                                        "action": {
                                        "type": "message",
                                        "label": "往南",
                                        "text": "南岡山往南"
                                        },
                                        "style": "primary",
                                        "offsetEnd": "none",
                                        "offsetTop": "none",
                                        "margin": "none",
                                        "gravity": "center",
                                        "offsetBottom": "none",
                                        "offsetStart": "none",
                                        "color": "#75C2F6"
                                    }
                                    ],
                                    "spacing": "none",
                                    "margin": "none",
                                    "offsetBottom": "none",
                                    "paddingBottom": "none",
                                    "borderWidth": "none",
                                    "justifyContent": "space-evenly"
                                }
                                ]
                            }
                            ]
                        }
                        }
                    ]
                    }
                )
    return flex_message

def show_orange():
    flex_message = FlexSendMessage(
            alt_text="橘起訖站",
            contents={
                        "type": "carousel",
                        "contents": [
                            {
                            "type": "bubble",
                            "size": "giga",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "(橘線)請選擇起訖站：",
                                    "weight": "bold",
                                    "size": "xl",
                                    "color": "#EE7214",
                                    "align": "center"
                                }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "separator"
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "O1西子灣",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#FB8B24",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往東",
                                            "text": "西子灣往東"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        }
                                        ],
                                        "spacing": "none",
                                        "margin": "none",
                                        "offsetBottom": "none",
                                        "paddingBottom": "none",
                                        "borderWidth": "none",
                                        "justifyContent": "space-evenly"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "O2鹽埕埔",
                                            "margin": "sm",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#FB8B24",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往東",
                                                "text": "鹽埕埔往東"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#1D5D9B"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往西",
                                                "text": "鹽埕埔往西"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#75C2F6"
                                            }
                                            ]
                                        },
                                        {
                                            "type": "separator",
                                            "margin": "xxl"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "text",
                                                "text": "O4市議會",
                                                "margin": "none",
                                                "align": "center",
                                                "gravity": "center",
                                                "size": "md",
                                                "color": "#FB8B24",
                                                "offsetEnd": "none",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "(舊址)",
                                                "margin": "none",
                                                "align": "center",
                                                "gravity": "center",
                                                "size": "md",
                                                "color": "#FB8B24",
                                                "offsetEnd": "none",
                                                "weight": "bold"
                                            }
                                            ],
                                            "justifyContent": "center",
                                            "alignItems": "center"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往東",
                                                "text": "市議會往東"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#1D5D9B"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往西",
                                                "text": "市議會往西"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#75C2F6"
                                            }
                                            ]
                                        }
                                        ],
                                        "spacing": "none",
                                        "margin": "none"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "O5美麗島",
                                            "margin": "sm",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#FB8B24",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往東",
                                                "text": "美麗島往東"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#1D5D9B"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往西",
                                                "text": "美麗島往西"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#75C2F6"
                                            }
                                            ]
                                        },
                                        {
                                            "type": "separator",
                                            "margin": "xxl"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "text",
                                                "text": "O6",
                                                "margin": "none",
                                                "align": "center",
                                                "gravity": "center",
                                                "size": "md",
                                                "color": "#FB8B24",
                                                "offsetEnd": "none",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "信義國小",
                                                "margin": "none",
                                                "align": "center",
                                                "gravity": "center",
                                                "size": "md",
                                                "color": "#FB8B24",
                                                "offsetEnd": "none",
                                                "weight": "bold"
                                            }
                                            ],
                                            "justifyContent": "center",
                                            "alignItems": "center"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往東",
                                                "text": "信義國小往東"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#1D5D9B"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往西",
                                                "text": "信義國小往西"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#75C2F6"
                                            }
                                            ]
                                        }
                                        ],
                                        "spacing": "none",
                                        "margin": "none"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "text",
                                                "text": "O7",
                                                "margin": "none",
                                                "align": "center",
                                                "gravity": "center",
                                                "size": "md",
                                                "color": "#FB8B24",
                                                "offsetEnd": "none",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "文化中心",
                                                "margin": "none",
                                                "align": "center",
                                                "gravity": "center",
                                                "size": "md",
                                                "color": "#FB8B24",
                                                "offsetEnd": "none",
                                                "weight": "bold"
                                            }
                                            ],
                                            "justifyContent": "center",
                                            "alignItems": "center"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往東",
                                                "text": "文化中心往東"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#1D5D9B"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往西",
                                                "text": "文化中心往西"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#75C2F6"
                                            }
                                            ]
                                        },
                                        {
                                            "type": "separator",
                                            "margin": "xxl"
                                        },
                                        {
                                            "type": "text",
                                            "text": "O8五塊厝",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#FB8B24",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往東",
                                                "text": "五塊厝往東"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#1D5D9B"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往西",
                                                "text": "五塊厝往西"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#75C2F6"
                                            }
                                            ]
                                        }
                                        ],
                                        "spacing": "none",
                                        "margin": "none"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "md"
                                    }
                                    ]
                                }
                                ]
                            }
                            },
                            {
                            "type": "bubble",
                            "size": "giga",
                            "body": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "(橘線)請選擇起訖站：",
                                    "weight": "bold",
                                    "size": "xl",
                                    "color": "#EE7214",
                                    "align": "center"
                                }
                                ]
                            },
                            "footer": {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "O9技擊館",
                                            "margin": "sm",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#FB8B24",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往東",
                                                "text": "技擊館往東"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#1D5D9B"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往西",
                                                "text": "技擊館往西"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#75C2F6"
                                            }
                                            ]
                                        },
                                        {
                                            "type": "separator",
                                            "margin": "xxl"
                                        },
                                        {
                                            "type": "text",
                                            "text": "O10衛武營",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#FB8B24",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往東",
                                                "text": "衛武營往東"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#1D5D9B"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往西",
                                                "text": "衛武營往西"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#75C2F6"
                                            }
                                            ]
                                        }
                                        ],
                                        "spacing": "none",
                                        "margin": "none"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "text",
                                                "text": "O11鳳山西站",
                                                "margin": "none",
                                                "align": "center",
                                                "gravity": "center",
                                                "size": "md",
                                                "color": "#FB8B24",
                                                "offsetEnd": "none",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "市議會",
                                                "margin": "none",
                                                "align": "center",
                                                "gravity": "center",
                                                "size": "md",
                                                "color": "#FB8B24",
                                                "offsetEnd": "none",
                                                "weight": "bold"
                                            }
                                            ],
                                            "justifyContent": "center",
                                            "alignItems": "center"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往東",
                                                "text": "鳳山西站往東"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#1D5D9B"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往西",
                                                "text": "鳳山西站往西"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#75C2F6"
                                            }
                                            ]
                                        },
                                        {
                                            "type": "separator",
                                            "margin": "xxl"
                                        },
                                        {
                                            "type": "text",
                                            "text": "O12鳳山",
                                            "margin": "none",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#FB8B24",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往東",
                                                "text": "鳳山往東"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#1D5D9B"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往西",
                                                "text": "鳳山往西"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#75C2F6"
                                            }
                                            ]
                                        }
                                        ],
                                        "spacing": "none",
                                        "margin": "none"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "O13大東",
                                            "margin": "sm",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#FB8B24",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往東",
                                                "text": "大東往東"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#1D5D9B"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往西",
                                                "text": "大東往西"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#75C2F6"
                                            }
                                            ]
                                        },
                                        {
                                            "type": "separator",
                                            "margin": "xxl"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "text",
                                                "text": "O14",
                                                "margin": "none",
                                                "align": "center",
                                                "gravity": "center",
                                                "size": "md",
                                                "color": "#FB8B24",
                                                "offsetEnd": "none",
                                                "weight": "bold"
                                            },
                                            {
                                                "type": "text",
                                                "text": "鳳山國中",
                                                "margin": "none",
                                                "align": "center",
                                                "gravity": "center",
                                                "size": "md",
                                                "color": "#FB8B24",
                                                "offsetEnd": "none",
                                                "weight": "bold"
                                            }
                                            ],
                                            "justifyContent": "center",
                                            "alignItems": "center"
                                        },
                                        {
                                            "type": "box",
                                            "layout": "vertical",
                                            "contents": [
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往東",
                                                "text": "鳳山國中往東"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#1D5D9B"
                                            },
                                            {
                                                "type": "button",
                                                "action": {
                                                "type": "message",
                                                "label": "往西",
                                                "text": "鳳山國中往西"
                                                },
                                                "style": "primary",
                                                "offsetEnd": "none",
                                                "offsetTop": "none",
                                                "margin": "none",
                                                "gravity": "center",
                                                "offsetBottom": "none",
                                                "offsetStart": "none",
                                                "color": "#75C2F6"
                                            }
                                            ]
                                        }
                                        ],
                                        "spacing": "none",
                                        "margin": "none"
                                    },
                                    {
                                        "type": "separator",
                                        "margin": "md"
                                    },
                                    {
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                        {
                                            "type": "text",
                                            "text": "OT1大寮",
                                            "margin": "sm",
                                            "align": "center",
                                            "gravity": "center",
                                            "size": "md",
                                            "color": "#FB8B24",
                                            "offsetEnd": "none",
                                            "weight": "bold"
                                        },
                                        {
                                            "type": "button",
                                            "action": {
                                            "type": "message",
                                            "label": "往西",
                                            "text": "大寮往西"
                                            },
                                            "style": "primary",
                                            "offsetEnd": "none",
                                            "offsetTop": "none",
                                            "margin": "none",
                                            "gravity": "center",
                                            "offsetBottom": "none",
                                            "offsetStart": "none",
                                            "color": "#1D5D9B"
                                        }
                                        ],
                                        "spacing": "none",
                                        "margin": "none"
                                    }
                                    ]
                                }
                                ]
                            }
                            }
                        ]
                        }
            )
    return flex_message

def show_MRT():
    flex_message = FlexSendMessage(
        alt_text="捷運功能",
        contents={                    
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://i.imgur.com/m0lm4wu.png",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                "type": "uri",
                "uri": "http://linecorp.com/"
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                {
                    "type": "text",
                    "text": "請選擇功能",
                    "size": "xxl",
                    "weight": "bold",
                    "align": "center",
                    "color": "#E3170D"
                }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "horizontal",
                "contents": [
                {
                    "type": "button",
                    "action": {
                    "type": "message",
                    "label": "高雄捷運圖",
                    "text": "高雄捷運圖"
                    },
                    "gravity": "center",
                    "color": "#1E90FF"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "紅線班次",
                        "text": "紅線班次"
                        },
                        "gravity": "center",
                        "color": "#FF0000",
                        "style": "secondary"
                    },
                    {
                        "type": "button",
                        "action": {
                        "type": "message",
                        "label": "橘線班次",
                        "text": "橘線班次"
                        },
                        "gravity": "center",
                        "color": "#FF7D40",
                        "style": "secondary"
                    }
                    ]
                }
                ]
            }
            }
        )
    return flex_message