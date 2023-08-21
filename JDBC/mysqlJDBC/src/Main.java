import java.sql.*;

public class Main {
    public static void main(String[] args ) {
        MySqlJDBC jbdc = new MySqlJDBC();
        try {
            jbdc.setConnection();;
            System.out.println("Conexao estabelecida...\n");
            jbdc.consulta();
            jbdc.inserirLinha();
            jbdc.consulta();
            jbdc.fecharConexao();
        } catch (SQLException e) {
            // TODO Auto-generated catch block
            System.out.println("Ocorreu um erro ao tentar acessar o banco: " + e);
        }
    }
}