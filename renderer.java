public class Renderer {

    private Shader shader;
    private Matrix4f viewMatrix = new Matrix4f();
    private Matrix4f projectionMatrix = new Matrix4f();

    public Renderer() {
        // Load shaders and set up camera matrices
        shader = new Shader("vertex.glsl", "fragment.glsl");
        viewMatrix.translate(0, 0, -5);
        projectionMatrix.perspective((float) Math.toRadians(60), 800f / 600f, 1f, 1000f);
    }

    public void render(Model model) {
        // Set up model and view matrices
        Matrix4f mvMatrix = new Matrix4f(viewMatrix).mul(model.getModelMatrix());
        shader.setUniform("mvMatrix", mvMatrix);
        shader.setUniform("projMatrix", projectionMatrix);

        // Bind textures and other OpenGL state
        // ...

        // Draw the model using the shader program
        glBindVertexArray(model.getVao());
        glDrawArrays(GL_TRIANGLES, 0, model.getNumVertices());
        glBindVertexArray(0);
    }

    public void setViewMatrix(Matrix4f viewMatrix) {
        this.viewMatrix = viewMatrix;
    }
}
