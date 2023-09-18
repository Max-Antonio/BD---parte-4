import java.sql.*;
import java.util.Scanner;

import javax.naming.spi.DirStateFactory.Result;


public class MySqlJDBC {

    private Connection conexao;

    public MySqlJDBC() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            System.out.println("Driver carregado");
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            System.out.println("Driver não localizado");
        } 
    }

    public void setConnection() throws SQLException {
        String host, bd, url, usuario, senha;
        host = "bdmysql.cv9n87dyspuf.us-east-1.rds.amazonaws.com";
        bd = "mysql";
        url = "jdbc:mysql://" + host + "/" + bd;
        usuario = "admin";
        senha = "admin123";
        conexao = DriverManager.getConnection(url, usuario, senha);
    }


    public void imprimeResultSet(ResultSet rs) throws SQLException {
        ResultSetMetaData meta = rs.getMetaData();
        for (int i = 1; i <= meta.getColumnCount(); i++) {
            System.out.print(meta.getColumnLabel(i) + ": " + meta.getColumnTypeName(i) + "\t");
        }
        System.out.println();
        while(rs.next()) {
            for (int i = 1; i <= meta.getColumnCount(); i++) {
                System.out.print(rs.getString(i) + "\t");
            }
            System.out.println();
        }
    }

    public void consulta() throws SQLException {
        Statement st = conexao.createStatement();
        String sql = "SELECT * FROM MyBook.Livro";
        ResultSet rs = st.executeQuery(sql);
        imprimeResultSet(rs);
    }

    public void fecharConexao() throws SQLException {
        conexao.close();
    }

    public void inserirLinha() throws SQLException {
        int numLinhas = 0;
        Statement st = conexao.createStatement();

        String sql1 = "SELECT * FROM MyBook.Livro";
        ResultSet rs = st.executeQuery(sql1);
        while(rs.next()) {
            numLinhas++;
        }

        String ISBN = "2000" + Integer.toString(numLinhas);

        String sql2 = "INSERT INTO MyBook.Livro (ISBN, nome, quantidade_leitores, existe_no_sistema, id_editora, id_administrador) VALUES(\"" + ISBN + "\", \"Livro" + ISBN +"\",\"10\",\"1\" ,\"1\", \"1\")";
        st.executeUpdate(sql2);
        System.out.println("\nInsercao feita com sucesso.\n");
    }

    public void transacao() {
    }
}
