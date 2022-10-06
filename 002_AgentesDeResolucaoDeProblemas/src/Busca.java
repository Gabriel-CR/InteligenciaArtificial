import java.util.Queue;
import java.util.Vector;

public class Busca {
    private Queue<Estado> borda;
    private Vector<Estado> explorados;

    public Boolean findBorda(Estado estado) {
        for (Estado est : this.borda) {
            if (est == estado) {
                return true;
            }
        }
        return false;
    }

    public Boolean findExplorados(Estado estado) {
        for (Estado est : this.borda) {
            if (est == estado) {
                return true;
            }
        }
        return false;
    }

    public Vector<Estado> buscaEmLargura(Problema problema) {
        this.borda.add(problema.getEstadoInicial());
        Vector<Estado> caminho = new Vector<>();

        while (true) {
            if (this.borda.isEmpty()) {
                return caminho;
            }

            No no = new No(borda.poll(), null, 0);
            this.explorados.add(no.getEstado());

            for (Estado est : problema.getEstados()) {
                No filho = new No(est, no, 1 + no.getCustoCaminho());
                if (this.findBorda(filho.getEstado()) || this.findExplorados(filho.getEstado())) {
                    if (filho.getEstado() == problema.getObjetivo()) {
                        return caminho;
                    }
                    this.borda.add(filho.getEstado());
                }
            }
        }
    }
}
