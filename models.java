import org.joml.Matrix4f;
import org.lwjgl.assimp.*;

public class Model {

    private AIScene scene;
    private Matrix4f modelMatrix = new Matrix4f();

    public Model(String filepath) {
        // Use Assimp to load the model file
        AIScene scene = aiImportFile(filepath, aiProcess_Triangulate);

        if (scene == null) {
            throw new RuntimeException("Error loading model " + filepath);
        }

        this.scene = scene;
    }

    public void setPosition(float x, float y, float z) {
        modelMatrix.translate(x, y, z);
    }

    public void setRotation(float angle, float x, float y, float z) {
        modelMatrix.rotate(angle, x, y, z);
    }

    public Matrix4f getModelMatrix() {
        return modelMatrix;
    }

    // ... rest of the model loading and manipulation code
}
