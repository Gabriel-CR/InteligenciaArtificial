import java.util.Map;
import java.util.Arrays;
import java.util.Vector;

public class Transicao {
    private Map<Estado, Estado[]> listaAdjacencias;

    public Transicao(Map<Estado, Estado[]> lista_adjacencias) {
        this.listaAdjacencias = lista_adjacencias;
    }

    public Map<Estado, Estado[]> getListaAdjacencias() {
        return listaAdjacencias;
    }

    public Vector<Estado[]> getEstados() {
        Vector<Estado[]> estados = new Vector<>();

        listaAdjacencias.entrySet().forEach(entry -> {
            estados.add(entry.getValue());
        });

        return estados;
    }

    public void getMap() {
        listaAdjacencias.entrySet().forEach(entry -> {
			System.out.println(entry.getKey().getNome() + " = " + Arrays.toString(entry.getValue()));
		});
    }
}
