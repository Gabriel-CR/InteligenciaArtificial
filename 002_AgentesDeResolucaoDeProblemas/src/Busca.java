import java.util.Queue;
import java.util.Vector;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

public class Busca {
    private Queue<Estado> borda = new LinkedList<Estado>();
    private Vector<Estado> explorados = new Vector<Estado>();

    // RETORNA UM NÓ, O CAMINHO SÃO OS SEUS PAIS
    /*public No buscaEmLargura(Problema problema) {
        this.borda.add(problema.estadoInicial);

        while (true) {
            if (this.borda.isEmpty()) {
                return null;
            }

            No no = new No(this.borda.poll(), null, 0);
            this.explorados.add(no.estado);

            Map<Estado, Estado[]> transicoes = new HashMap<>(problema.transicoes);

            for (int i = 0; i < problema.transicoes.get(no.estado).length; i++) {
                No filho = new No(problema.transicoes.get(no.estado)[i], no, no.custoCaminho + 1);

                if (this.borda.contains(filho.estado) == false && this.explorados.contains(filho.estado) == false) {
                    if (filho.estado == problema.objetivo) {
                        return filho;
                    }
                    this.borda.add(filho.estado);
                }
            }
        }
    }*/

    // LINHAS QUE MUDAM 6, 13, 14
    public No buscaCustoUniforme(Problema problema) {
        borda.add(problema.estadoInicial);

        while (true) {
            if (borda.isEmpty()) {
                return null;
            }

            No no = new No(borda.poll(), null, 0);

            if (no.estado == problema.objetivo) {
                return no;
            }

            explorados.add(no.estado);

            for (int i = 0; i < problema.transicoes.get(no.estado).length; i++) {
                No filho = new No(problema.transicoes.get(no.estado)[i], no, no.custoCaminho);
                if (this.borda.contains(filho.estado) == false && this.explorados.contains(filho.estado) == false) {
                    borda.add(filho.estado);
                } else if () {

                }
            }
        }
    }
}
