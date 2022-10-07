public class No {
    public Estado estado;
    public No pai;
    public int custoCaminho;

    public No(Estado estado, No pai, int custoCaminho) {
        this.estado = estado;
        this.pai = pai;
        this.custoCaminho = custoCaminho;
    }
}
