
from dash import html
from dash import dcc
import dash_bootstrap_components as dbc
import dash_daq as daq

ControlsCard = dbc.Card([
    dbc.CardBody([
        dbc.Row([
            dbc.Col([
                html.H6("Select Threshold value"),
                daq.Slider(
                    id='Threshold_slider',
                    min=0,
                    max=1000,
                    step=10,
                    value=300,
                    handleLabel={"showCurrentValue": True,"label": "Threshold"},
                    vertical=True
                ),
            ],
            ),
            dbc.Col([
                html.H6("Select # of colors"),
                daq.Slider(
                    id='number_colors_slider',
                    min=1,
                    max=200,
                    step=1,
                    value=50,
                    handleLabel={"showCurrentValue": True,"label": "Colors"},
                    vertical=True
                ),
            ],

            ),
            dbc.Col([
                html.H6("Select the number of dimentions"),
                daq.Slider(
                    id='dim_slider',
                    min=1,
                    max=6,
                    step=1,
                    value=3,
                    handleLabel={"showCurrentValue": True,"label": "Dim"},
                    vertical=True
                ),
            ],

            ),
            dbc.Col([
                html.H6("Select smoothing factor"),
                daq.Slider(
                    id='array_size_slider',
                    min=5,
                    max=500,
                    step=1,
                    value=30,
                    handleLabel={"showCurrentValue": True,"label": "Smoothing"},
                    vertical=True
                ),
            ],
            ),
            dbc.Col([
                html.H6("select array type"),
                dcc.RadioItems(
                options=[
                    {'label': 'linear1', 'value': 1},
                    {'label': 'linear2', 'value': 2},
                    {'label': 'radial1', 'value': 3},
                    {'label': 'radial2', 'value': 4}
                ],
                value=1,
                id = "Array_type"
                )
            ],
            ),
            dbc.Col([
                html.H6("Sort colors?"),
                daq.ToggleSwitch(
                    id='sort-toggle-switch',
                    value=False
                ),
                html.H6("Discrete colors?"),
                daq.ToggleSwitch(
                    id='discrete-toggle-switch',
                    value=False
                ),
                html.H6("Unique colors for every patch?"),
                daq.ToggleSwitch(
                    id='unique-color-switch',
                    value=False
                ),
            ],
            ),
            dbc.Col([
                html.H6("select sorting value"),
                dcc.RadioItems(
                options=[
                    {'label': 'Red', 'value': 0},
                    {'label': 'Green', 'value': 1},
                    {'label': 'Blue', 'value': 2}
                ],
                value=1,
                id = "color_sort_value"
                )
            ],
            ),
        ])
    ]),
    dbc.Row(
        [
        dbc.Col([
            html.Button('Submit', id='Control_submit', n_clicks=0)
        ])
    ])
])


upload_card = dbc.Card(
    [
        dbc.CardBody([
            dcc.Upload(
                id='upload-image',
                children=html.Div([
                    'Drag and Drop or ',
                    html.A('Select Files')
                ]),
                style={
                    'width': '100%',
                    'height': '60px',
                    'lineHeight': '60px',
                    'borderWidth': '1px',
                    'borderStyle': 'dashed',
                    'borderRadius': '5px',
                    'textAlign': 'center',
                    'margin': '10px'
                },
                multiple=False
            ),
        ]),
        dbc.Spinner([
            dbc.CardImg(id='card_image', bottom=True,
                        style={"height": "230px",
                              "width": "auto",
                               'align': 'center'}
                       ),
        ],
        color="success"
        )
    ],
)


def layout():
    layout = html.Div(
        id = "app-body",
        className = "app-body",
        children = [
            dcc.Store(id='colors', storage_type='local'),
            dbc.Row(
            [
                dbc.Col([
                    upload_card,
                ],
                    width = 4,
                    style={'textAlign': 'center'}
                ),
                dbc.Col(ControlsCard,
                    width = 7,
                        style={'textAlign': 'center'}
                )
            ],
            ),
            dbc.Row([
                dbc.Col(
                    [
                        dcc.Graph(id = 'output-image-transformed',
                                  style = {'display':'none'})
                    ],
                    width={"size": 6, "offset": 3},
                ),
            ])
        ]
    )

    return layout


