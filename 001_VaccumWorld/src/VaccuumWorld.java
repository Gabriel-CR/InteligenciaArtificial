public class VaccuumWorld {
    public static void main(String[] args) throws Exception {

        Environment env = new Environment(true, true, true);
        // Perception p = new Perception(env.isAgentLocation(), false);
        Agent a = new Agent();
        // Action act;

        while(env.isDirtyA() || env.isDirtyB()) {
            System.out.println(env);
                env.update(
                    a.perceives(
                        new Perception(env.isAgentLocation(), env.isAgentLocation() ? env.isDirtyA() : env.isDirtyB())
                    )
                );
        }
        System.out.println(env);
    }
}
