package com.mtruehle.hawkathonpulsetransmitter;

import android.content.Context;
import android.hardware.Camera;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
//import android.hardware.camera2.CameraAccessException;
//import android.hardware.camera2.CameraCharacteristics;
//import android.hardware.camera2.CameraDevice;
//import android.hardware.camera2.CameraManager;
//import android.hardware.camera2.params.StreamConfigurationMap;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.util.Log;
import android.util.Size;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.View;
import android.view.Menu;
import android.view.MenuItem;

public class MainActivity extends AppCompatActivity {

    private SensorManager mSensorManager;
    private Sensor mLightSensor;
    private float mLightLevel;

    public String IPADDRESS = "192.168.43.211";
//    public String IPADDRESS = "10.253.117.172";
    public int PORT = 8888;

//    public CameraDevice cameraDevice;
//    public CameraManager cameraManager;

    public int WIDTH = 100; //pixels?
    public int HEIGHT = 200; //pixels?

    public SurfaceView surfaceView;
    public SurfaceHolder surfaceViewHolder;
    public Camera camera;
//    public View image;

    public int averageIndex = 0;
    int[] readings = new int[10];
    int readingsIndex = 0;

    public Camera.PreviewCallback previewCallback;
    public SurfaceHolder.Callback surfaceCallback;


    protected void onCreate(Bundle savedInstanceState) {

        Log.d("asdf", "onCreate called");
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);


//        camera = Camera.open();
        }




//        FloatingActionButton fab = (FloatingActionButton) findViewById(R.id.fab);
//        fab.setOnClickListener(new View.OnClickListener() {
//            @Override
//            public void onClick(View view) {
//                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
//                        .setAction("Action", null).show();
//            }
//        });

//        mSensorManager = (SensorManager)getSystemService(SENSOR_SERVICE);
//        mLightSensor = mSensorManager.getDefaultSensor(Sensor.TYPE_LIGHT);

//        SensorEventListener listener = new SensorEventListener() {
//            @Override
//            public void onSensorChanged(SensorEvent sensorEvent) {
//                mLightLevel = sensorEvent.values[0];
//                Log.d("light_sensor", String.valueOf(mLightLevel));
//            }
//
//            @Override
//            public void onAccuracyChanged(Sensor sensor, int i) {
//
//            }
//        };
//        mSensorManager.registerListener(listener, mLightSensor, SensorManager.SENSOR_DELAY_FASTEST);

//        CameraManager cameraManager = (CameraManager) this.getSystemService(Context.CAMERA_SERVICE);
//        try {
//            for (String cameraId: cameraManager.getCameraIdList()) {
//                CameraCharacteristics characteristics = cameraManager.getCameraCharacteristics(cameraId);
//
//                Integer facing = characteristics.get(CameraCharacteristics.LENS_FACING);
//                if (facing != null && facing == CameraCharacteristics.LENS_FACING_FRONT) {
//                    continue; // "continue"-s back to the top of the loop if the camera is the front-facing one; forces use of back-facing one.
//                }
//
//                StreamConfigurationMap configs = characteristics.get(CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP);
//
//                if (configs == null) {
//                    continue;
//                }
//
//
//
//
//
//            }
//
//        } catch (CameraAccessException ex) {
//            ex.printStackTrace();
//        }

//    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    @Override
    public void onPause() {
        Log.d("asdf", "onPause");
        super.onPause();
        camera.release();
        camera = null;
    }

    @Override
    public void onResume() {
        Log.d("asdf", "onResume");
        super.onResume();

        //        surfaceView = new SurfaceView(this);
        Log.e("asdf", "about to make sview");
        surfaceView = (SurfaceView) findViewById(R.id.sview);
        surfaceViewHolder = surfaceView.getHolder();
        Log.e("asdf", "holder gotten");


        previewCallback = new Camera.PreviewCallback() {
            @Override
            public void onPreviewFrame(byte[] bytes, Camera camera) {
                Log.d("asdf", "onPreviewFrame");
                if (bytes == null) {
                    return;
                }
                Camera.Size size = camera.getParameters().getPreviewSize();
                if (size == null) {
                    Log.d("camera", "size null");
                }
                int redAverage = bytesToRedAverage(bytes.clone(), size.height, size.width);

                if (redAverage == 0 || redAverage == 255) {
                    return; // disregard full and 0 brightness.
                }

                Log.d("red_average", String.valueOf(redAverage));

//                int past_average = rollingAverage(redAverage);
//                if (redAverage < 10 + past_average) {
//                    Log.d("beats", "BEAT?");
//                }
                String listForAsync[] = new String[] {IPADDRESS, String.valueOf(PORT), String.valueOf(redAverage)};

                new SocketAsync().execute(listForAsync);
            }
        };

        surfaceCallback = new SurfaceHolder.Callback() {
            @Override
            public void surfaceCreated(SurfaceHolder holder) {
                Log.d("asdf", "surfaceCreated");
                try {
                    camera.setPreviewDisplay(surfaceViewHolder);
                    camera.setPreviewCallback(previewCallback);
                } catch (Exception e) {
                    Log.e("surface", "surfaceCreated error");
                }
            }

            @Override
            public void surfaceChanged(SurfaceHolder holder, int format, int width, int height) {
                Log.d("asdf", "surfaceChanged");
                Camera.Parameters params = camera.getParameters();
//                params.setFlashMode(Camera.Parameters.FLASH_MODE_TORCH);
                Camera.Size size = getSmallestPreviewSize(width, height, params);
                if (size != null) {
                    params.setPreviewSize(size.width, size.height);
                }
                camera.setParameters(params);
                camera.startPreview();
            }


            @Override
            public void surfaceDestroyed(SurfaceHolder holder) {
                //empty constructor
            }


        };


        surfaceViewHolder.addCallback(surfaceCallback);
        surfaceViewHolder.setType(SurfaceHolder.SURFACE_TYPE_PUSH_BUFFERS); // TODO: fix
        Log.e("asdf", "callback added");




        camera = Camera.open();
    }

    public int bytesToRedAverage(byte[] bytes, int width, int height) {
        // math-code from stranger on stackoverflow like two years ago; forgot to note down where. I shamelessly copy-pasted the number values :P.
        Log.d("asdf", "bytesToRedAverage");
        int area = width*height;
        int sum = 0;
        for (int j = 0, yp = 0; j < height; j++) {
            int uvp = area + (j >> 1) * width, u = 0, v = 0;
            for (int i = 0; i < width; i++, yp++) {
                int y = (0xff & bytes[yp]) - 16;
                if (y < 0) y = 0;
                if ((i & 1) == 0) {
                    v = (0xff & bytes[uvp++]) - 128;
                    u = (0xff & bytes[uvp++]) - 128;
                }
                int y1192 = 1192 * y;
                int r = (y1192 + 1634 * v);
                int g = (y1192 - 833 * v - 400 * u);
                int b = (y1192 + 2066 * u);

                if (r < 0) r = 0;
                else if (r > 262143) r = 262143;
                if (g < 0) g = 0;
                else if (g > 262143) g = 262143;
                if (b < 0) b = 0;
                else if (b > 262143) b = 262143;

                int pixel = 0xff000000 | ((r << 6) & 0xff0000) | ((g >> 2) & 0xff00) | ((b >> 10) & 0xff);
                int red = (pixel >> 16) & 0xff;
                sum += red;
            }
        }
        return (sum/area);
    }

    public int rollingAverage(int newValue) {
        Log.d("asdf", "rollingAverage");
        int sum = 0;
        int rl = readings.length;
        for (int i = 0; i<rl; i++) {
            sum += readings[i];
        }
        int currentAverage = sum/rl;
        readings[readingsIndex] = newValue;
        readingsIndex++;
        if (readingsIndex >= rl) {
            readingsIndex = 0;
        }
        return currentAverage;
    }

    public Camera.Size getSmallestPreviewSize(int width, int height, Camera.Parameters params) {
        Log.d("asdf", "getSmallestPreviewSize");
        Camera.Size result = null;
        for (Camera.Size size : params.getSupportedPreviewSizes()) {
            if (size.width <= width && size.height <= height) {
                if (result == null) {
                    result = size;
                } else {
                    if ((size.width*size.height) < (result.width*result.height)) {
                        result = size;
                    }
                }
            }
        }
        return result;
    }
}

