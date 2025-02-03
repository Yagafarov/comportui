# 3POD robot arm

## Description

This project is an interactive application for simulating the kinematics of a robot using Three.js and WebGL. Users can input the lengths of the links and the angles of the joints, and the application will compute and display the end position of the robot in 3D space.

[Demo live](https://robot-kinematics.netlify.app/)

[Creatored by CodeWithDin](https://anodra.uz)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Yagafarov/robot-kinematics.git
   ```

2. Navigate to the project directory:

   ```bash
   cd robot-kinematics
   ```

3. Open `index.html` in your web browser.

## Usage

- Enter the link lengths (l1, l2, l3) and joint angles (θ1, θ2, θ3) in the respective fields.
- Use the sliders for quick adjustments.
- Click on the "Forward Kinematics" or "Inverse Kinematics" buttons to compute and display the robot's position.
- The "Reset" button will return all values to their initial states.

## Technologies

- [Three.js](https://threejs.org/) - 3D graphics library.
- [WebGL](https://webgl.org/) - API for rendering 2D and 3D graphics.
- JavaScript - programming language for application logic.

## Contribution

If you would like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
