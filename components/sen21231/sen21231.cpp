#include "sen21231.h"
#include "esphome/core/log.h"

namespace esphome {
namespace sen21231_sensor {

static const char *const TAG = "sen21231_sensor.sensor";

void Sen21231Sensor::update() { this->read_data_(); }

void Sen21231Sensor::dump_config() {
    ESP_LOGCONFIG(TAG, "SEN21231:");
    LOG_I2C_DEVICE(this);
    if (this->is_failed()) {
        ESP_LOGE(TAG, "Communication with SEN21231 failed!");
    }
    ESP_LOGI(TAG, "SEN21231: %s", this->is_failed() ? "FAILED" : "OK");
    LOG_UPDATE_INTERVAL(this);
}

void Sen21231Sensor::read_data_() {
    person_sensor_results_t results;
    this->read_bytes(PERSON_SENSOR_I2C_ADDRESS, (uint8_t *)&results,
                     sizeof(results));
    ESP_LOGD(TAG, "SEN21231: %d faces detected", results.num_faces);
//    this->publish_state(results.num_faces);
    if (results.num_faces == 1) {
        ESP_LOGD(TAG, "SEN21231: box confidence is facing : %d",
                 results.faces[0].box_confidence);
        ESP_LOGD(TAG, "SEN21231: box pixel to the left: %d",
                 results.faces[0].box_left);
        ESP_LOGD(TAG, "SEN21231: box pixel to the top %d",
                 results.faces[0].box_top);
        ESP_LOGD(TAG, "SEN21231: box pixel to the right: %d",
                 results.faces[0].box_right);
        ESP_LOGD(TAG, "SEN21231: box pixel to the bottom: %d",
                 results.faces[0].box_bottom);
        ESP_LOGD(TAG, "SEN21231: confidence it is the ID: %d",
                 results.faces[0].id_confidence);
        ESP_LOGD(TAG, "SEN21231: detected ID: %d",
                 results.faces[0].id);
        ESP_LOGD(TAG, "SEN21231: is facing towards camera: %d",
                 results.faces[0].is_facing);
    }
    unsigned num_facing_camera = 0;
    for (unsigned j = 0; j<results.num_faces;j++) {
      if (results.faces[j].is_facing) {
        num_facing_camera++;
      }
    }
    if (this->people_sensor_ != nullptr)
      this->people_sensor_->publish_state(results.num_faces);
    if (this->people_facing_camera_ != nullptr)
      this->people_facing_camera_->publish_state(num_facing_camera); 
      //TODO 
    if (this->people_box_confidence_ != nullptr)
      this->people_box_confidence_->publish_state(num_facing_camera);
    this->status_clear_warning();
}

} // namespace sen21231_sensor
} // namespace esphome