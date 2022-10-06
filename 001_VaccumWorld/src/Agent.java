public class Agent {
    public Agent() {
        super();
    }

    public Action perceives(Perception p) {
        Action a = new Action();

        if(p.isLocation() && p.isDirty()) {
            a = this.act("ASPIRAR");
        } else if (p.isLocation() && !p.isDirty()){
            a = this.act("MOVE_DIR");
        }

        if(!p.isLocation() && p.isDirty()) {
            a = this.act("ASPIRAR");
        } else if(!p.isLocation() && !p.isDirty()) {
            a = this.act("MOVE_ESQ");
        }

        return a;
    }
    
    private Action act(String act) {
        return new Action(act);
    }
}
