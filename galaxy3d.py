
import numpy as np
import plotly.graph_objects as go


def create_galaxy():

    total_stars = 12000
    arms = 4
    max_radius = 15

    radius = np.random.power(1.5, total_stars) * max_radius
    arm_number = np.random.randint(0, arms, total_stars)

    angle = radius * 0.55 + arm_number * (2 * np.pi / arms)
    angle += np.random.normal(0, 0.18, total_stars)

    x = radius * np.cos(angle)
    y = radius * np.sin(angle)
    z = np.random.normal(0, 0.25, total_stars)

    # Galactic core
    core_count = 5000
    core_x = np.random.normal(0, 0.65, core_count)
    core_y = np.random.normal(0, 0.65, core_count)
    core_z = np.random.normal(0, 0.35, core_count)

    # Bright nucleus
    nucleus_count = 1200
    nucleus_x = np.random.normal(0, 0.18, nucleus_count)
    nucleus_y = np.random.normal(0, 0.18, nucleus_count)
    nucleus_z = np.random.normal(0, 0.12, nucleus_count)

    x = np.concatenate([x, core_x, nucleus_x])
    y = np.concatenate([y, core_y, nucleus_y])
    z = np.concatenate([z, core_z, nucleus_z])

    brightness = np.concatenate([
        np.random.uniform(1, 8, total_stars),
        np.random.uniform(8, 15, core_count),
        np.random.uniform(15, 25, nucleus_count)
    ])

    fig = go.Figure()

    # Galaxy stars
    fig.add_trace(go.Scatter3d(
        x=x, y=y, z=z,
        mode="markers",
        marker=dict(
            size=1.5,
            color=brightness,
            colorscale="Plasma",
            opacity=0.8,
            showscale=False
        ),
        name="Galaxy Stars"
    ))

    # Golden nucleus
        # Golden Glowing Galactic Nucleus
    fig.add_trace(go.Scatter3d(
        x=[0],
        y=[0],
        z=[0],
        mode="markers",
        marker=dict(
            size=18,
            color="#FFD700",
            opacity=1
        ),
        name="Bright Galactic Center"
    ))

    # Glowing Nebula Effect
    fig.add_trace(go.Scatter3d(
        x=nucleus_x,
        y=nucleus_y,
        z=nucleus_z,
        mode="markers",
        marker=dict(
            size=9,
            color="#FFA500",
            opacity=0.18
        ),
        name="Golden Star Glow"
    ))

    # Colorful Nebula Clouds
    nebula_colors = ["#A020F0", "#00BFFF", "#FF1493"]

    for color in nebula_colors:

        cloud_count = 1800
        cloud_angle = np.random.uniform(0, 2 * np.pi, cloud_count)
        cloud_radius = np.random.normal(9, 2, cloud_count)

        cloud_x = cloud_radius * np.cos(cloud_angle)
        cloud_y = cloud_radius * np.sin(cloud_angle)
        cloud_z = np.random.normal(0, 0.9, cloud_count)

        fig.add_trace(go.Scatter3d(
            x=cloud_x,
            y=cloud_y,
            z=cloud_z,
            mode="markers",
            marker=dict(
                size=4,
                color=color,
                opacity=0.4
            ),
            name="Nebula Cloud"
        ))
    # 3D Planet and Orbit

    orbit_angle = np.linspace(0, 2 * np.pi, 200)

    orbit_radius = 7

    orbit_x = orbit_radius * np.cos(orbit_angle)
    orbit_y = orbit_radius * np.sin(orbit_angle)
    orbit_z = np.zeros(200)

    # Planet orbit path
    fig.add_trace(go.Scatter3d(
        x=orbit_x,
        y=orbit_y,
        z=orbit_z,
        mode="lines",
        line=dict(
            color="#00BFFF",
            width=4
        ),
        name="Planet Orbit"
    ))

    # Planet position
    planet_x = orbit_radius
    planet_y = 0
    planet_z = 0

    fig.add_trace(go.Scatter3d(
        x=[planet_x],
        y=[planet_y],
        z=[planet_z],
        mode="markers",
        marker=dict(
            size=12,
            color="#00BFFF",
            opacity=1
        ),
        name="Blue Planet"
    ))
    fig.update_layout(
        title="Interactive 3D Spiral Galaxy",
        template="plotly_dark",
        paper_bgcolor="#050510",
        scene=dict(
            bgcolor="#050510",
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode="data"
        ),
        margin=dict(l=0, r=0, t=50, b=0),
        height=650
    )

    print("NEBULA CLOUDS LOADED!")

    
    # Moving Planet Animation

    frames = []

    for i in range(60):
        angle = 2 * np.pi * i / 60

        planet_x = 7 * np.cos(angle)
        planet_y = 7 * np.sin(angle)

        frames.append(
            go.Frame(
                data=[
                    go.Scatter3d(
                        x=[planet_x],
                        y=[planet_y],
                        z=[0],
                        mode="markers",
                        marker=dict(
                            size=12,
                            color="#00BFFF",
                            opacity=1
                        ),
                        name="Blue Planet"
                    )
                ],
                traces=[7],
                name=str(i)
            )
        )

    fig.frames = frames

    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                showactive=False,
                buttons=[
                    dict(
                        label="▶ Play Planet",
                        method="animate",
                        args=[
                            None,
                            dict(
                                frame=dict(duration=80, redraw=True),
                                transition=dict(duration=0),
                                fromcurrent=True,
                                mode="immediate"
                            )
                        ]
                    ),
                    dict(
                        label="⏸ Pause",
                        method="animate",
                        args=[
                            [None],
                            dict(
                                frame=dict(duration=0, redraw=False),
                                mode="immediate"
                            )
                        ]
                    )
                ]
            )
        ]
    )

    print("PLANET ANIMATION READY!")

    return fig
