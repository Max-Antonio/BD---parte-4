package com.example;

import java.sql.*;


public class MySqlJDBC {

    private Connection conexao;

    public MySqlJDBC() {
        try {
            Class.forName("com.mysql.jdbc.Driver");
            System.out.println("Driver carregado");
        } catch (ClassNotFoundException e) {
            // TODO Auto-generated catch block
            System.out.println("Driver não localizado");
        } 
    }

    public void setConnection() throws SQLException {
        String host, bd, url, usuario, senha;
        host = "localhost:3306";
        bd = "bdmysql";
        url = "jdbc:mysql://" + host + "/" + bd;
        usuario = "admin";
        senha = "admin123";
        conexao = DriverManager.getConnection(url, usuario, senha);
    }

    public void consulta() throws SQLException {
        Statement st = conexao.createStatement();
        String sql = "SELECT * FROM MyBook.Livro";
        ResultSet rs = st.executeQuery(sql);
        while(rs.next()) {
            String ISBN, nome, qtd_leitores, existe_no_sistema, id_editora, id_administrador;
            System.out.println(rs.getRow() + " ");
            ISBN = rs.getString(1);
            nome = rs.getString(2);
            qtd_leitores = Integer.toString(rs.getInt(3));
            existe_no_sistema = Integer.toString(rs.getInt(4));
            id_editora = rs.getString(5);
            id_administrador = rs.getString(6);
            System.out.println(ISBN + "\t" + nome + "\t" + qtd_leitores + "\t" + existe_no_sistema + "\t" + id_editora + "\t" + id_administrador);
        }
    }

    public void inserirLinha() {
    }

    public void transacao() {
    }
}