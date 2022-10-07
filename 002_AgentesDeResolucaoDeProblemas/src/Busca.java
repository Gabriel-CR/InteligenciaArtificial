import java.util.Queue;
import java.util.Vector;
import java.util.LinkedList;

public class Busca {
    private Queue<Estado> borda;
    private Vector<Estado> explorados;

    // RETORNA UM NÓ, O CAMINHO SÃO OS SEUS PAIS
    public No buscaEmLargura(Problema problema) {
        borda = new LinkedList<Estado>();
        explorados = new Vector<Estado>();
        this.borda.add(problema.estadoInicial);

        while (true) {
            if (this.borda.isEmpty()) {
                return null;
            }

            No no = new No(this.borda.poll(), null, 0);
            this.explorados.add(no.estado);

            for (Estado est : problema.transicoes.get(no.estado)) {
                No filho = new No(est, no, no.custoCaminho + 1);

                if (this.borda.contains(filho.estado) == false && this.explorados.contains(filho.estado) == false) {
                    if (filho.estado == problema.objetivo) {
                        return filho;
                    }
                    this.borda.add(filho.estado);
                }
            }
        }
    }

    // LINHAS QUE MUDAM 6, 13, 14
}
