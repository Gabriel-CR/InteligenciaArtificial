import java.util.Vector;

public class App {
    public static void main(String[] args) throws Exception {
        Data dados = new Data();
        Transicao transicoes = new Transicao(dados.getListaAdjacencias());
        Busca busca = new Busca();

        Problema problema = new Problema(
            dados.getEstados(), 
            new Estado("Arad"), 
            transicoes.getListaAdjacencias(), 
            new Estado("Bucharest")
        );

        Vector<Estado> caminho = busca.buscaEmLargura(problema);

        for (Estado e : caminho) {
            System.out.println(e.getNome());
        }
    }
}
