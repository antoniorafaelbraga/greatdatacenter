package br.ufc.great.model;

/**
 * Created by rafaelbraga on 05/12/16.
 */

public class Status {

    int codStatus;
    String strStatus;

    public int getCodStatus() {
        return codStatus;
    }

    public void setCodStatus(int codStatus) {
        this.codStatus = codStatus;
    }

    public String getStrStatus() {
        return strStatus;
    }

    public void setStrStatus(String strStatus) {
        this.strStatus = strStatus;
    }

    @Override
    public String toString() {
    	return "{\"codStatus\" : \""+codStatus+"\", \"strStatus\" : \""+strStatus+"\"}";
    }
}
