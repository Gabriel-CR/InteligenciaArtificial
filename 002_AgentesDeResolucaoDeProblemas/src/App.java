public class App {
    public static void main(String[] args) throws Exception {
        Data dados = new Data();
        Transicao transicoes = new Transicao(dados.getListaAdjacencias());

        Problema problema = new Problema(
            dados.getEstados(), 
            dados.getEstados()[2],  // Arad
            transicoes.getListaAdjacencias(), 
            dados.getEstados()[13]  // Bucharest
        );

        // System.out.println(problema);

        Busca busca = new Busca();

        No caminho = new No(busca.buscaEmLargura(problema));

        while (caminho != null) {
            System.out.println(caminho.estado.getNome());
            caminho = caminho.pai;
        }
    }
}
