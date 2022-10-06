public class Environment {
    private boolean isDirtyA;
    private boolean isDirtyB;
    private boolean agentLocation;
    
    public Environment(boolean isDirtyA, boolean isDirtyB, boolean agentLocation) {
        this.isDirtyA = isDirtyA;
        this.isDirtyB = isDirtyB;
        this.agentLocation = agentLocation;
    }

    public boolean isDirtyA() {
        return isDirtyA;
    }

    public void setDirtyA(boolean isDirtyA) {
        this.isDirtyA = isDirtyA;
    }

    public boolean isDirtyB() {
        return isDirtyB;
    }

    public void setDirtyB(boolean isDirtyB) {
        this.isDirtyB = isDirtyB;
    }

    public boolean isAgentLocation() {
        return agentLocation;
    }

    public void setAgentLocation(boolean agentLocation) {
        this.agentLocation = agentLocation;
    }

    public void update(Action act) {
        if(act.getName().equals("ASPIRAR")) {
            if(this.isAgentLocation()) {
                this.setDirtyA(false);
            } else {
                this.setDirtyB(false);
            }
        }

        if(act.getName().equals("MOVE_DIR")) {
            if(this.isAgentLocation()) {
                this.setAgentLocation(false);
            }
        }

        if(act.getName().equals("MOVE_ESQ")) {
            if(!this.isAgentLocation()) {
                this.setAgentLocation(true);
            }
        }
    }

    @Override
    public String toString() {
        return "Environment [agentLocation = " + agentLocation + ", \tisDirtyA = " + isDirtyA + ", \tisDirtyB = " + isDirtyB  + "]";
    }
}
