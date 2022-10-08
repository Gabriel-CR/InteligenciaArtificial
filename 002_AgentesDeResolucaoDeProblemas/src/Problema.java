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

    @Override
    public String toString() {
        String os = new String();

        os += "Estados: ";
        for (Estado estado : this.estados) {
            os += estado.getNome() + ", ";
        }

        os += "Estado inicial: " + this.estadoInicial.getNome() + "\n";

        os += "Transições: \n";

        for (Estado estado : this.transicoes.keySet()) {
            os += estado.getNome() + " -> ";

            for (Estado estadoAdjacente : this.transicoes.get(estado)) {
                os += estadoAdjacente.getNome() + ", ";
            }

            os += "\n";
        }

        os += "Objetivo: " + this.objetivo.getNome() + "\n";

        return os;
    }
}
