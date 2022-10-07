import java.util.Map;

public class Problema {
    public Estado[] estados;
    public Estado estadoInicial;
    public Map<Estado, Estado[]> transicoes;
    public Estado objetivo;
    public int custoCaminho;

    public Problema(Estado[] estados, Estado estadoInicial, Map<Estado, Estado[]> transicoes, Estado objetivo) {
        this.estados = estados;
        this.estadoInicial = estadoInicial;
        this.transicoes = transicoes;
        this.objetivo = objetivo;
    }
}
