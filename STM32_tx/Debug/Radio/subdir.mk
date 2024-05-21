################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Radio/board.c \
../Radio/delay.c \
../Radio/gpio-board.c \
../Radio/gpio.c \
../Radio/rtc-board.c \
../Radio/spi-board.c \
../Radio/sx1276-board.c \
../Radio/timer.c \
../Radio/utilities.c 

OBJS += \
./Radio/board.o \
./Radio/delay.o \
./Radio/gpio-board.o \
./Radio/gpio.o \
./Radio/rtc-board.o \
./Radio/spi-board.o \
./Radio/sx1276-board.o \
./Radio/timer.o \
./Radio/utilities.o 

C_DEPS += \
./Radio/board.d \
./Radio/delay.d \
./Radio/gpio-board.d \
./Radio/gpio.d \
./Radio/rtc-board.d \
./Radio/spi-board.d \
./Radio/sx1276-board.d \
./Radio/timer.d \
./Radio/utilities.d 


# Each subdirectory must supply rules for building sources it contributes
Radio/%.o Radio/%.su: ../Radio/%.c Radio/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32L476xx -c -I../Core/Inc -I"C:/Users/kryst/Pulpit/Nauka/Systemy_wbudowane/STM32/CubeIDE/BEKO_W2B/Radio" -I../Drivers/STM32L4xx_HAL_Driver/Inc -I../Drivers/STM32L4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Radio

clean-Radio:
	-$(RM) ./Radio/board.d ./Radio/board.o ./Radio/board.su ./Radio/delay.d ./Radio/delay.o ./Radio/delay.su ./Radio/gpio-board.d ./Radio/gpio-board.o ./Radio/gpio-board.su ./Radio/gpio.d ./Radio/gpio.o ./Radio/gpio.su ./Radio/rtc-board.d ./Radio/rtc-board.o ./Radio/rtc-board.su ./Radio/spi-board.d ./Radio/spi-board.o ./Radio/spi-board.su ./Radio/sx1276-board.d ./Radio/sx1276-board.o ./Radio/sx1276-board.su ./Radio/timer.d ./Radio/timer.o ./Radio/timer.su ./Radio/utilities.d ./Radio/utilities.o ./Radio/utilities.su

.PHONY: clean-Radio

