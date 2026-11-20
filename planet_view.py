
import numpy as np
import pyvista as pv
from pathlib import Path


def create_planet_scene():

    folder = Path(__file__).parent / "textures"

    planets = [
        ("Earth", "earth.jpg", (-5, 0, 0), 1.25),
        ("Mars", "mars.jpg", (-1.7, 0, 0), 0.9),
        ("Jupiter", "jupiter.jpg", (2, 0, 0), 1.8),
        ("Saturn", "saturn.jpg", (7, 0, 0), 1.5),
    ]

    plotter = pv.Plotter(window_size=(1100, 650))
    plotter.set_background("#03040c")

    for name, filename, position, radius in planets:

        texture_path = folder / filename

        if not texture_path.exists():
            raise FileNotFoundError(
                f"Texture missing: {texture_path}"
            )

        sphere = pv.Sphere(
            radius=radius,
            center=position,
            theta_resolution=120,
            phi_resolution=120
        )

        sphere = sphere.texture_map_to_sphere(
            inplace=False
        )

        texture = pv.read_texture(str(texture_path))

        plotter.add_mesh(
            sphere,
            texture=texture,
            smooth_shading=True,
            name=name
        )
                # Realistic Saturn Flat Rings
        if name == "Saturn":

            ring_layers = [
                (1.75, 2.05, "#8C7658", 0.65),
                (2.08, 2.30, "#D6C19A", 0.85),
                (2.35, 2.65, "#B49A70", 0.8),
                (2.72, 2.78, "#03040c", 0.0),
                (2.82, 3.05, "#D8C39A", 0.75),
                (3.08, 3.35, "#A68B65", 0.7),
                (3.38, 3.50, "#D6C19A", 0.6)
            ]

            for inner, outer, color, opacity in ring_layers:

                if opacity == 0:
                    continue

                ring = pv.Disc(
                    center=position,
                    inner=inner,
                    outer=outer,
                    normal=(0.25, 0.65, 0.72),
                    r_res=1,
                    c_res=300
                )

                plotter.add_mesh(
                    ring,
                    color=color,
                    opacity=opacity,
                    smooth_shading=True
                )

            ring_data = [
                (2.0, "#D8C39A"),
                (2.35, "#A68B65"),
                (2.7, "#E8D5AD"),
                (3.05, "#B8A078"),
                (3.4, "#D6C19A")
            ]

            for ring_radius, color in ring_data:

                ring = pv.ParametricTorus(
                    ringradius=ring_radius,
                    crosssectionradius=0.035
                )

                ring.translate(position, inplace=True)
                ring.rotate_x(25, inplace=True)
                ring.rotate_y(15, inplace=True)

                plotter.add_mesh(
                    ring,
                    color=color,
                    opacity=0.9,
                    smooth_shading=True
                )
    # Background star field
    np.random.seed(42)

    star_positions = np.random.uniform(
        low=[-18, -10, -8],
        high=[18, 10, 8],
        size=(1800, 3)
    )

    stars = pv.PolyData(star_positions)

    plotter.add_points(
        stars,
        color="white",
        point_size=2,
        render_points_as_spheres=True
    )

    plotter.camera_position = "xy"
    plotter.camera.zoom(1.15)

    return plotter
