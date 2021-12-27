import dash
from dash.dependencies import Input, Output, State
from assets import layout as lo
from assets import transform as tf
from assets import dash_reusable_components as drc
import dash_bootstrap_components as dbc
from dash import html
import flask
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
import io
import json 
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots

default_css = "https://codepen.io/chriddyp/pen/bWLwgP.css"

external_stylesheets = [dbc.themes.BOOTSTRAP]
server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, server=server, prevent_initial_callbacks=True, suppress_callback_exceptions=True)

app.layout = lo.layout()

@app.callback(Output('card_image', 'src'),
              Output('colors', 'data'),
              Input('upload-image', 'contents'))
def define_colors(contents):
    photo = html.Img(src=contents)
    string = contents.split(';base64,')[-1]
    im_pil = drc.b64_to_pil(string)
    img_data = {}
    colors = Counter(im_pil.getdata())
    rounded_colors = tf.round_colors(colors)
    #make colors hex for storage
    hex_colors = {"#{0:02x}{1:02x}{2:02x}".format(x[0][0], x[0][1], x[0][2]):x[1] for x in colors.items()}
#     hex_rounded_colors = {"#{0:02x}{1:02x}{2:02x}".format(x[0][0], x[0][1], x[0][2]):x[1] for x in rounded_colors.items()}
    img_data['colors'] = hex_colors
#     img_data['rounded_colors'] = hex_rounded_colors
    return(contents, img_data)

@app.callback(Output("output-image-transformed", "figure"),
              Output("output-image-transformed", "style"),
              Input('Control_submit', "n_clicks"),
              State('Threshold_slider', "value"),
              State('number_colors_slider', "value"),
              State('array_size_slider', "value"),
              State("Array_type", "value"),
              State('sort-toggle-switch', "value"),
              State("color_sort_value", "value"),
              State('colors', 'data'),
              State('discrete-toggle-switch', "value"),
              State('dim_slider', "value"),
              State('unique-color-switch', "value")
             )
def transform_photo(n, threshold, num_colors, array_size, array_type, sort, sort_value, colors, discrete_colors, dim, unique_colors):
    a1 = eval(f'tf.make_array{array_type}')(array_size)
    if discrete_colors:
        d = array_size/num_colors
        a1 = (a1/d).astype(int)
#     print(a1)

    dim = dim
    fig = make_subplots(rows=dim, cols=dim, 
                        shared_xaxes=True, 
                        shared_yaxes=True,
                       vertical_spacing=0,
                       horizontal_spacing=0)
    if not unique_colors:
        cm1 = tf.make_color_map_and_array(colors['colors'], threshold, sort, sort_value, num_colors)
    
    for c in range(1, dim+1):
        for r in range(1, dim+1):
            if unique_colors:
                cm1 = tf.make_color_map_and_array(colors['colors'], threshold, sort, sort_value, num_colors)
            fig.add_trace(
                go.Heatmap(
                    z = a1, colorscale = cm1, showscale=False
                ),
            row=r, col=c
            )
    fig.update_layout(
                      height = 800,
                      width = 800
                     )
    fig.update_xaxes(showticklabels=False, visible=False)
    fig.update_yaxes(showticklabels=False)
    return fig, {'display': 'block', 'textAlign': 'center'}
    
  
if __name__ == '__main__':
    layout2 = lo.layout()
    app.layout = layout2
    app.run_server(debug=True,
    port = 8999
    )