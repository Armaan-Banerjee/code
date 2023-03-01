import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class SimpleServlet extends HttpServlet {
    
    protected void doGet(HttpServletRequest request, HttpServletResponse response) 
            throws ServletException, IOException {
        response.getWriter().write("Hello World!");
    }
    
}

import org.apache.catalina.LifecycleException;
import org.apache.catalina.startup.Tomcat;

public class SimpleServer {

    public static void main(String[] args) throws LifecycleException {

        Tomcat tomcat = new Tomcat();
        tomcat.setPort(9080);
        tomcat.addWebapp("/", "./");

        tomcat.addServlet("/", "SimpleServlet", new SimpleServlet());
        tomcat.getConnector();

        tomcat.start();
        tomcat.getServer().await();

    }

}
