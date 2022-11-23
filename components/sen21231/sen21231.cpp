#include "sen21231.h"
#include "esphome/core/log.h"

namespace esphome {
namespace sen21231_sensor {

static const char *TAG = "sen21231_sensor.sensor";

void Sen21231Sensor::setup() {}

void Sen21231Sensor::update() {}

void Sen21231Sensor::dump_config() {
    ESP_LOGCONFIG(TAG, "SEN21231:");
    LOG_I2C_DEVICE(this);
    if (this->is_failed()) {
        ESP_LOGE(TAG, "Communication with SEN21231 failed!");
    }
    ESP_LOGI(TAG, "SEN21231: %s", this->is_failed() ? "FAILED" : "OK");
}

} // namespace sen21231_sensor
} // namespace esphome
