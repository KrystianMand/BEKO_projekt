/*
 * app_template.h
 *
 */

#ifndef INC_APP_TEMPLATE_H_
#define INC_APP_TEMPLATE_H_

void app_main(void);
void rx_loop(void);
void tx_loop(void);
void tx_message(uint8_t* msg, size_t size);

#endif /* INC_APP_TEMPLATE_H_ */
