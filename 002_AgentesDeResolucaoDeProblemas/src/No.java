public class No {
    private Estado estado;
    private No pai;
    private int custoCaminho;

    public No(Estado estado, No pai, int custoCaminho) {
        this.estado = estado;
        this.pai = pai;
        this.custoCaminho = custoCaminho;
    }

    public Estado getEstado() {
        return estado;
    }
    public No getPai() {
        return pai;
    }
    public int getCustoCaminho() {
        return custoCaminho;
    }
    
}
