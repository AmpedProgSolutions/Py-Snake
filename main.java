import org.lwjgl.glfw.GLFW;
import org.lwjgl.glfw.GLFWErrorCallback;
import org.lwjgl.opengl.GL;
import static org.lwjgl.glfw.GLFW.*;
import static org.lwjgl.opengl.GL11.*;

public class Window {

    private long window;

    public Window() {
        // Initialize GLFW and register an error callback
        GLFWErrorCallback.createPrint(System.err).set();

        if (!glfwInit()) {
            throw new IllegalStateException("Unable to initialize GLFW");
        }

        // Create a window and set its properties
        window = glfwCreateWindow(800, 600, "My 3D Engine", 0, 0);
        glfwMakeContextCurrent(window);
        glfwSwapInterval(1);

        // Initialize OpenGL
        GL.createCapabilities();

        glEnable(GL_DEPTH_TEST);
        glDepthFunc(GL_LESS);

        // Set up a simple perspective projection
        glMatrixMode(GL_PROJECTION);
        glLoadIdentity();
        glFrustum(-1, 1, -1, 1, 1, 1000);

        // Switch to modelview matrix and set up default camera
        glMatrixMode(GL_MODELVIEW);
        glLoadIdentity();
        gluLookAt(0, 0, 0, 0, 0, -1, 0, 1, 0);
    }

    public long getWindow() {
        return window;
    }

    public void swapBuffers() {
        glfwSwapBuffers(window);
    }

    public boolean shouldClose() {
        return glfwWindowShouldClose(window);
    }

    public void destroy() {
        glfwDestroyWindow(window);
        glfwTerminate();
        GLFWErrorCallback.createPrint(System.err).set(null).free();
    }
}
