################################################################################
# Automatically-generated file. Do not edit!
# Toolchain: GNU Tools for STM32 (10.3-2021.10)
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../Radio/sx1276/sx1276.c 

OBJS += \
./Radio/sx1276/sx1276.o 

C_DEPS += \
./Radio/sx1276/sx1276.d 


# Each subdirectory must supply rules for building sources it contributes
Radio/sx1276/%.o Radio/sx1276/%.su: ../Radio/sx1276/%.c Radio/sx1276/subdir.mk
	arm-none-eabi-gcc "$<" -mcpu=cortex-m4 -std=gnu11 -g3 -DDEBUG -DUSE_HAL_DRIVER -DSTM32L476xx -c -I../Core/Inc -I"C:/Users/kryst/Pulpit/Nauka/Systemy_wbudowane/STM32/CubeIDE/BEKO_W2B/Radio" -I../Drivers/STM32L4xx_HAL_Driver/Inc -I../Drivers/STM32L4xx_HAL_Driver/Inc/Legacy -I../Drivers/CMSIS/Device/ST/STM32L4xx/Include -I../Drivers/CMSIS/Include -O0 -ffunction-sections -fdata-sections -Wall -fstack-usage -MMD -MP -MF"$(@:%.o=%.d)" -MT"$@" --specs=nano.specs -mfpu=fpv4-sp-d16 -mfloat-abi=hard -mthumb -o "$@"

clean: clean-Radio-2f-sx1276

clean-Radio-2f-sx1276:
	-$(RM) ./Radio/sx1276/sx1276.d ./Radio/sx1276/sx1276.o ./Radio/sx1276/sx1276.su

.PHONY: clean-Radio-2f-sx1276

