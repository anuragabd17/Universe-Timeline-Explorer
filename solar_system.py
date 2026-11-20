
import numpy as np
import plotly.graph_objects as go


def create_solar_system():

    # Planet orbital distances (visual scale)
    planets = [
        ("Earth", 5, 7, "#3399FF", 0.0),
        ("Mars", 7, 6, "#FF5533", 1.0),
        ("Jupiter", 10, 13, "#D6A36A", 2.0),
        ("Saturn", 13, 11, "#E8D5AD", 3.0)
    ]

    fig = go.Figure()

    # Sun at the center
    fig.add_trace(go.Scatter3d(
        x=[0], y=[0], z=[0],
        mode="markers+text",
        text=["SUN"],
        textposition="top center",
        marker=dict(
            size=25,
            color="#FFD700",
            opacity=1
        ),
        name="Sun"
    ))

    # Planet starting positions
    for name, radius, size, color, phase in planets:

        angle = phase

        x = radius * np.cos(angle)
        y = radius * np.sin(angle)

        fig.add_trace(go.Scatter3d(
            x=[x], y=[y], z=[0],
            mode="markers+text",
            text=[name],
            textposition="top center",
            marker=dict(
                size=size,
                color=color,
                opacity=1
            ),
            name=name
        ))

    # Draw orbital paths
    orbit_angle = np.linspace(0, 2 * np.pi, 200)

    for name, radius, size, color, phase in planets:

        fig.add_trace(go.Scatter3d(
            x=radius * np.cos(orbit_angle),
            y=radius * np.sin(orbit_angle),
            z=np.zeros(200),
            mode="lines",
            line=dict(
                color="rgba(180,180,220,0.35)",
                width=2
            ),
            name=name + " Orbit",
            showlegend=False
        ))

    # Background stars
    np.random.seed(42)

    star_x = np.random.uniform(-17, 17, 1000)
    star_y = np.random.uniform(-17, 17, 1000)
    star_z = np.random.uniform(-5, 5, 1000)

    fig.add_trace(go.Scatter3d(
        x=star_x,
        y=star_y,
        z=star_z,
        mode="markers",
        marker=dict(
            size=1.5,
            color="white",
            opacity=0.7
        ),
        name="Stars",
        showlegend=False
    ))

    # Animation frames
    frames = []

    total_frames = 120

    for i in range(total_frames):

        frame_data = []

        for name, radius, size, color, phase in planets:

            angle = (
                2 * np.pi * i / total_frames
                + phase
            )

            x = radius * np.cos(angle)
            y = radius * np.sin(angle)

            frame_data.append(go.Scatter3d(
                x=[x],
                y=[y],
                z=[0],
                mode="markers+text",
                text=[name],
                textposition="top center",
                marker=dict(
                    size=size,
                    color=color,
                    opacity=1
                )
            ))

        frames.append(go.Frame(
            data=frame_data,
            traces=[1, 2, 3, 4],
            name=str(i)
        ))

    fig.frames = frames

    # Layout and controls
    fig.update_layout(
        title="Interactive 3D Solar System",
        template="plotly_dark",
        paper_bgcolor="#03040c",
        height=700,
        margin=dict(l=0, r=0, t=50, b=0),

        scene=dict(
            bgcolor="#03040c",
            xaxis=dict(visible=False, range=[-16, 16]),
            yaxis=dict(visible=False, range=[-16, 16]),
            zaxis=dict(visible=False, range=[-7, 7]),
            aspectmode="cube"
        ),

        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                x=0.05,
                y=1.05,
                buttons=[
                    dict(
                        label="▶ Play",
                        method="animate",
                        args=[
                            None,
                            dict(
                                frame=dict(
                                    duration=60,
                                    redraw=True
                                ),
                                transition=dict(duration=0),
                                fromcurrent=True
                            )
                        ]
                    ),
                    dict(
                        label="⏸ Pause",
                        method="animate",
                        args=[
                            [None],
                            dict(
                                frame=dict(duration=0),
                                mode="immediate"
                            )
                        ]
                    )
                ]
            )
        ]
    )

    return fig
