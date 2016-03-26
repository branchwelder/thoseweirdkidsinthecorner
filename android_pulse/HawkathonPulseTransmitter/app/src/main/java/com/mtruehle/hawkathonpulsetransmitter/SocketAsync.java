package com.mtruehle.hawkathonpulsetransmitter;

import android.os.AsyncTask;
import android.util.Log;

import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;

/**
 * Created by matt on 3/26/16.
 */
public class SocketAsync extends AsyncTask<String, Void, Void> {

    @Override
    protected Void doInBackground(String[] strings) {
//        int PORT = 8888;
        int BUFFER_LENGTH = 128;
        Log.d("socketAsync", "in doInBackground");
        Socket socket = null;
        DataOutputStream dataOutputStream = null;
        String ipAddress = strings[0];
        int port = Integer.parseInt(strings[1]);
        String messageToSend = strings[2];
        try {
            Log.d("socketAsync", "about to start socket");
            socket = new Socket(ipAddress, port);
            Log.d("socketAsync", "started socket");
            dataOutputStream = new DataOutputStream(socket.getOutputStream());
            dataOutputStream.writeUTF(messageToSend);
            Log.d("socketAsync", "wrote UTF in socket async");
            dataOutputStream.close();
            socket.close();
        } catch (IOException ex) {
            Log.d("socketAsync", "error: " + ex.getMessage());
            return null;
        }
        return null;
    }
}
