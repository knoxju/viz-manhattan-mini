from flask import Flask, render_template, request, redirect

import fetching                 # my fetching.py file

app = Flask(__name__)

app.config.update(
    DEBUG=True,
)



@app.route('/')
def main():
    return render_template('index.html')

# @app.route('/index')
# def index():
#     return render_template('index.html')

@app.route('/live_buses')
def live_buses():
    nyc = fetching.nyc_current()
    plotdf = nyc[['MonitoredVehicleJourney_PublishedLineName',
                  'MonitoredVehicleJourney_VehicleLocation_Latitude',
                  'MonitoredVehicleJourney_VehicleLocation_Longitude']]

    # add this for plot (may not be using yet)
    plotdf = plotdf.assign(intensity=0.2);
    #data = list(plotdf.itertuples())
    #data = plotdf.values.tolist()
    data = plotdf[['MonitoredVehicleJourney_VehicleLocation_Latitude',
                   'MonitoredVehicleJourney_VehicleLocation_Longitude']].values.tolist()
    return render_template('live_buses.html', data=data)

@app.route('/live_example')
def live_example():
    return render_template('live_example.html')


@app.route('/page1')
def page1():
  return redirect('/')

@app.route('/page2')
def page2():
  return redirect('/')

@app.route('/page3')
def page3():
  return redirect('/')




if __name__ == '__main__':
    app.run(port=33507)