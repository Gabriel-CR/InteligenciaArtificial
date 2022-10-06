import java.util.Map;

public class Problema {
    private Estado[] estados;
    private Estado estadoInicial;
    private Map<Estado, Estado[]> transicoes;
    private Estado objetivo;
    private int custoCaminho;

    public Problema(Estado[] estados, Estado estadoInicial, Map<Estado, Estado[]> transicoes, Estado objetivo) {
        this.estados = estados;
        this.estadoInicial = estadoInicial;
        this.transicoes = transicoes;
        this.objetivo = objetivo;
    }
    
    public Estado[] getEstados() {
        return estados;
    }

    public Estado getEstadoInicial() {
        return estadoInicial;
    }

    public Map<Estado, Estado[]> getTransicoes() {
        return transicoes;
    }

    public Estado getObjetivo() {
        return objetivo;
    }
    
    public int getCustoCaminho() {
        return custoCaminho;
    }
}
