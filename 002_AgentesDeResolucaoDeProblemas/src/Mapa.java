import java.util.Map;

public class Mapa {
    private Map<Estado, Estado[]> cidades;

    public Mapa (Map<Estado, Estado[]> cidades) {
        this.cidades = cidades;
    }

    public Map<Estado, Estado[]> getCidades() {
        return this.cidades;
    }
}