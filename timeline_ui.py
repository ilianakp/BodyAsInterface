import numpy as np
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
import open3d as o3d
import copy

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

pcl= o3d.io.read_point_cloud("model0.ply")
pcl1= o3d.io.read_point_cloud("model1_tocombine - Cloud.ply")
pcl2= o3d.io.read_point_cloud("model2_tocombine - Cloud.ply")
pcl3= o3d.io.read_point_cloud("model3_tocombine - Cloud.ply")
pcl_room= o3d.io.read_point_cloud("part_room - Cloud.ply")
pcl_room2= o3d.io.read_point_cloud("part_room2 - Cloud.ply")
mesh = o3d.io.read_triangle_mesh("com_rd.ply")

voxel = 0.05

# function to create a figure of a point cloud
def create_cloud(cloud, downsample):
    downpcd = cloud.voxel_down_sample(voxel_size=voxel)
    downpcd = copy.deepcopy(downpcd).translate((0,0,0), relative=False)
    array = np.asarray(downpcd.points)
    cl_array = np.asarray(downpcd.colors)
    return go.Figure(data=[go.Scatter3d(x=array[:, 0], y=array[:, 1], z=array[:, 2],mode='markers', marker=dict(color=cl_array, size=1))])

def create_mesh(mesh):
    mesh_pts = np.asarray(mesh.vertices)
    mesh_tris = np.asarray(mesh.triangles)
    return go.Figure(data=[go.Mesh3d(name='3D Model', x = mesh_pts[:, 0], y = mesh_pts[:, 1], z = mesh_pts[:, 2], opacity=0.5)])


fig = create_cloud(pcl, voxel)
fig.update_layout(autosize=False, width=1400, height=900, showlegend=False, scene_aspectmode='data', uirevision = True, scene = dict(xaxis = dict(title='', showbackground=False,showticklabels=False),yaxis = dict(title='', showbackground=False,showticklabels=False),zaxis = dict(title='', showbackground=False,showticklabels=False))),
fig1 = create_cloud(pcl1, voxel)
fig1.update_layout(showlegend=False, scene_aspectmode='data', uirevision = True, scene = dict(xaxis = dict(title='', showbackground=False,showticklabels=False),yaxis = dict(title='', showbackground=False,showticklabels=False),zaxis = dict(title='', showbackground=False,showticklabels=False))),
fig2 = create_cloud(pcl2, voxel)
fig2.update_layout(showlegend=False, scene_aspectmode='data', uirevision = True, scene = dict(xaxis = dict(title='', showbackground=False,showticklabels=False),yaxis = dict(title='', showbackground=False,showticklabels=False),zaxis = dict(title='', showbackground=False,showticklabels=False))),
fig3 = create_cloud(pcl3, voxel)
fig3.update_layout(showlegend=False, scene_aspectmode='data', uirevision = True, scene = dict(xaxis = dict(title='', showbackground=False,showticklabels=False),yaxis = dict(title='', showbackground=False,showticklabels=False),zaxis = dict(title='', showbackground=False,showticklabels=False))),
figroom = create_cloud(pcl_room, voxel)
figroom.update_layout(showlegend=False, scene_aspectmode='data', uirevision = True, scene = dict(xaxis = dict(title='', showbackground=False,showticklabels=False),yaxis = dict(title='', showbackground=False,showticklabels=False),zaxis = dict(title='', showbackground=False,showticklabels=False))),
figroom2 = create_cloud(pcl_room2, voxel)
figroom2.update_layout(showlegend=False, scene_aspectmode='data', uirevision = True, scene = dict(xaxis = dict(title='', showbackground=False,showticklabels=False),yaxis = dict(title='', showbackground=False,showticklabels=False),zaxis = dict(title='', showbackground=False,showticklabels=False))),
fig_mesh = create_mesh(mesh)


#html.Div([
#                               html.Div(dcc.Graph(id='3d_mesh', figure=m), style={'height': '99vh', 'width':'99vw'}),
#                           ], style=dict(uirevision=True, horizontalAlignment='middle')),

app.layout = html.Div([
    html.Div([
            html.P("TIME CHIMERA", style={ 'align':'center','fontSize':'30px'})]),
    dcc.Slider(id='my-slider', min=0, max=6, step=1, value=0,),
    html.Div(id='slider-output-container')
])

@app.callback(
    dash.dependencies.Output('slider-output-container', 'children'),
    [dash.dependencies.Input('my-slider', 'value')])
def update_output(value):
    if (value==0):
        #ig.add_trace(fig_mesh)
        return html.Div(dcc.Graph(id='3d_scat', figure=fig), style={'height': 'auto', 'width': 'auto'})
    if (value==1):
        #fig1.add_trace(fig_mesh)
        return html.Div(dcc.Graph(id='3d_scat', figure=fig1), style={'height': 'auto', 'width': 'auto'})
    if (value==2):
        #fig2.add_trace(fig_mesh)
        return html.Div(dcc.Graph(id='3d_scat', figure=fig2), style={'height': 'auto', 'width': 'auto'})
    if (value==3):
        #fig3.add_trace(fig_mesh)
        return html.Div(dcc.Graph(id='3d_scat', figure=fig3), style={'height': 'auto', 'width': 'auto'})
    if (value==4):
        #figroom.add_trace(fig_mesh)
        return html.Div(dcc.Graph(id='3d_scat', figure=figroom), style={'height': 'auto', 'width': 'auto'})
    if (value==5):
        #figroom2.add_trace(fig_mesh)
        return html.Div(dcc.Graph(id='3d_scat', figure=figroom2), style={'height': 'auto', 'width': 'auto'})


#old app.layout
#html.Div([
#    html.Div(dcc.Graph(id='3d_scat', figure=fig), style={'height': 'auto', 'width': 'auto'})],
#    style=dict(display='flex', flexWrap='nowrap', verticalAlignment='middle', horizontalAlignment='middle'))

if __name__ == '__main__':
    app.run_server(debug=True)